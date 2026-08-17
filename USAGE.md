# .NET usage guide

The [README](README.md) contains installation instructions and the complete function index. This guide focuses on safe production patterns.

## Register and reuse the clients

Register x402api once in your application's dependency-injection container. The generated APIs use `HttpClientFactory` and should be resolved from DI.

```csharp
using Microsoft.Extensions.Hosting;
using X402Api.Client;
using X402Api.Extensions;

string token = Environment.GetEnvironmentVariable("X402API_TENANT_API_KEY")
    ?? throw new InvalidOperationException(
        "X402API_TENANT_API_KEY is required");

using IHost host = Host.CreateDefaultBuilder(args)
    .ConfigureX402Api((_, options) =>
    {
        options.AddTokens(new BearerToken(token));
        options.UseProvider<RateLimitProvider<BearerToken>, BearerToken>();
        options.AddX402ApiHttpClients(
            client => client.Timeout = TimeSpan.FromSeconds(15),
            builder => builder
                .AddRetryPolicy(2)
                .AddCircuitBreakerPolicy(5, TimeSpan.FromSeconds(30))
        );
    })
    .Build();
```

The retry policy is optional and is not enabled unless you configure it. Use separate service providers or token providers when your process acts for multiple tenant credentials.

## Create and retrieve a charge

```csharp
var request = new DynamicChargeCreate(
    Guid.Parse("00000000-0000-4000-8000-000000000001"),
    "https://merchant.example.com/premium-report",
    new List<DynamicChargePrice>
    {
        new("base_usdc", "1000000")
    },
    900,
    metadata: new Option<Dictionary<string, object>?>(
        new Dictionary<string, object>
        {
            ["order_id"] = "order-123"
        })
);

IProgrammaticChargesApi chargesApi =
    host.Services.GetRequiredService<IProgrammaticChargesApi>();

string idempotencyKey = "charge-order-123-v1";
IChargesCreateApiResponse createResponse =
    await chargesApi.ChargesCreateAsync(idempotencyKey, request);

if (!createResponse.TryCreated(out DynamicChargeResponse? charge))
{
    throw new InvalidOperationException(
        $"x402api returned {(int)createResponse.StatusCode}: " +
        createResponse.RawContent);
}

IChargesRetrieveApiResponse retrieveResponse =
    await chargesApi.ChargesRetrieveAsync(charge.ChargeId);
DynamicChargeResponse? sameCharge = retrieveResponse.Ok();
```

Prices use atomic-unit strings, not floating point. For example, `"1000000"` represents one token for an asset with six decimals.

## Pagination and HTTP headers

```csharp
IOrdersAndPaymentsApi paymentsApi =
    host.Services.GetRequiredService<IOrdersAndPaymentsApi>();
string? cursorValue = null;

do
{
    Option<string> cursor = cursorValue is null
        ? default
        : new Option<string>(cursorValue);
    IPaymentsListApiResponse response =
        await paymentsApi.PaymentsListAsync(
            cursor: cursor,
            pageSize: new Option<int>(100));

    if (!response.TryOk(out List<SettlementJob>? payments))
    {
        throw new InvalidOperationException(
            $"x402api returned {(int)response.StatusCode}: " +
            response.RawContent);
    }

    foreach (SettlementJob payment in payments)
    {
        Process(payment);
    }

    cursorValue = response.Headers.TryGetValues(
            "X-X402API-Next-Cursor",
            out IEnumerable<string>? values)
        ? values.First()
        : null;
} while (cursorValue is not null);
```

Treat the cursor as opaque and pass it back unchanged. The same pattern applies to orders, payment observations, receiving addresses, resources, and resource versions. Every operation accepts a `CancellationToken`.

## Error handling

Documented HTTP outcomes are returned as response wrappers rather than thrown as exceptions. Use status helpers and typed accessors:

```csharp
IPaymentsRetrieveApiResponse response =
    await paymentsApi.PaymentsRetrieveAsync(paymentId, cancellationToken);

if (response.IsOk)
{
    SettlementJob? payment = response.Ok();
}
else
{
    ApiErrorEnvelope? error = response.Default();
    string? requestId = response.Headers.TryGetValues(
            "X-Request-ID",
            out IEnumerable<string>? values)
        ? values.FirstOrDefault()
        : null;
    LogApiError(response.StatusCode, error, response.RawContent, requestId);
}
```

Network, timeout, cancellation, and unexpected client failures can still throw. `*OrDefaultAsync` methods return `null` when no documented response wrapper can be produced.

## Idempotency and retries

Mutations require keys of 8-160 characters matching `[A-Za-z0-9._:-]+`. Persist the key with the intent you are executing.

- New intended mutation: generate a new key.
- Timeout or connection reset after sending: retry the identical body with the same key.
- Known validation failure: fix the request and use a new key.
- Uncertain durable outcome: call `IIdempotencyApi.IdempotencyGetOutcomeAsync(key)`.

Bound retry attempts, use exponential backoff with jitter, respect `Retry-After`, and normally retry only connection failures plus HTTP `408`, `429`, `500`, `502`, `503`, and `504`. The generated `AddRetryPolicy` helper handles transient HTTP failures but uses a simple bounded retry; supply your own Polly policy when you need jitter or `Retry-After` awareness.

## Public endpoints

These endpoints do not need a tenant key. They can be resolved from an x402api host registration that does not call `AddTokens`:

```csharp
using IHost publicHost = Host.CreateDefaultBuilder(args)
    .ConfigureX402Api()
    .Build();

IFacilitatorDiscoveryApi facilitator =
    publicHost.Services.GetRequiredService<IFacilitatorDiscoveryApi>();
IFacilitatorGetSupportedApiResponse supported =
    await facilitator.FacilitatorGetSupportedAsync();

IOrdersAndPaymentsApi publicPayments =
    publicHost.Services.GetRequiredService<IOrdersAndPaymentsApi>();
IReceiptVerificationKeysRetrieveApiResponse keys =
    await publicPayments.ReceiptVerificationKeysRetrieveAsync();
```

Do not edit generated files under `src/X402Api/` or `docs/`; update the OpenAPI contract or generator configuration instead.
