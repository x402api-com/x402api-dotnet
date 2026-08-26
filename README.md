# x402api .NET SDK

Official server-side .NET client for the [x402api public API](https://api.x402api.com/openapi/openapi.json). It provides typed request and response models for programmatic x402 charges, resources, receiving addresses, payments, receipts, and wallet balances.

The NuGet package is `X402Api`, targets .NET 8+, and integrates with `Microsoft.Extensions.Hosting`, dependency injection, `HttpClientFactory`, and optional Polly policies. The production base URL is `https://api.x402api.com`.

> Package registry publishing is separate from SDK generation. Until the first NuGet release is available, reference the project from this repository.

## Installation

From NuGet after a release is published:

```bash
dotnet add package X402Api --version 1.0.0
```

From source today:

```bash
git clone https://github.com/x402api-com/x402api-dotnet.git
dotnet add reference x402api-dotnet/src/X402Api/X402Api.csproj
```

## Authentication and dependency injection

Create a scoped tenant API key and register it as a bearer token. Keep it in a server-side secret store; do not ship tenant credentials in browser, mobile, or desktop applications.

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using X402Api.Api;
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
    })
    .Build();

IProgrammaticChargesApi chargesApi =
    host.Services.GetRequiredService<IProgrammaticChargesApi>();
```

`FacilitatorGetSupportedAsync` and `ReceiptVerificationKeysRetrieveAsync` are public; the generated host still accepts the same client registration for them. All other operations use tenant bearer authentication.

Tenant API keys must also grant the exact scope documented by each operation:

- charges: `commerce:write` to create and `commerce:read` to retrieve;
- network-fee quotes and resource reads: `resources:read`;
- resource creation and new versions: `resources:write`;
- orders: `orders:read`;
- payment readiness: `payment-controls:read`;
- payments, observations, and receipts: `payments:read`;
- receiving-address capabilities and lists: `wallets:read`; and
- wallet balances: `balances:read`.

The SDK excludes dashboard-only mutations that require a human tenant owner with recent step-up. A tenant API key cannot call those operations regardless of its scopes.

## Quick start: create a charge

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using X402Api.Api;
using X402Api.Client;
using X402Api.Extensions;
using X402Api.Model;

string token = Environment.GetEnvironmentVariable("X402API_TENANT_API_KEY")
    ?? throw new InvalidOperationException(
        "X402API_TENANT_API_KEY is required");

using IHost host = Host.CreateDefaultBuilder(args)
    .ConfigureX402Api((_, options) =>
    {
        options.AddTokens(new BearerToken(token));
        options.UseProvider<RateLimitProvider<BearerToken>, BearerToken>();
    })
    .Build();

var request = new DynamicChargeCreate(
    Guid.Parse("00000000-0000-4000-8000-000000000001"),
    "https://merchant.example.com/premium-report",
    new List<DynamicChargePrice>
    {
        new("base_usdc", "1000000")
    },
    900
);

IProgrammaticChargesApi api =
    host.Services.GetRequiredService<IProgrammaticChargesApi>();
IChargesCreateApiResponse response = await api.ChargesCreateAsync(
    "charge-example-001",
    request
);

if (!response.IsCreated)
{
    throw new InvalidOperationException(
        $"x402api returned {(int)response.StatusCode}: {response.RawContent}");
}

DynamicChargeResponse? charge = response.Created();
Console.WriteLine(charge);
```

The first argument to `ChargesCreateAsync` is the `Idempotency-Key`. Use a new key for each intended mutation. If the outcome is uncertain, retry the identical payload with the same key.

## Response metadata and pagination

API methods return a response interface with `StatusCode`, `Headers`, `RawContent`, status helpers such as `IsOk`, and typed body accessors such as `Ok()` or `Created()`:

```csharp
using X402Api.Client;

IOrdersAndPaymentsApi paymentsApi =
    host.Services.GetRequiredService<IOrdersAndPaymentsApi>();

IPaymentsListApiResponse response =
    await paymentsApi.PaymentsListAsync(pageSize: new Option<int>(25));

if (response.IsOk)
{
    foreach (SettlementJob payment in response.Ok())
    {
        Console.WriteLine(payment);
    }
}

if (response.Headers.TryGetValues(
        "X-X402API-Next-Cursor",
        out IEnumerable<string>? cursors))
{
    string cursor = cursors.First();
    IPaymentsListApiResponse nextPage = await paymentsApi.PaymentsListAsync(
        cursor: new Option<string>(cursor),
        pageSize: new Option<int>(25)
    );
}
```

Cursors are opaque. Pass them back unchanged; do not decode or construct them. Every method accepts a `CancellationToken`.

The generated client does not enable retries by default. Configure retry, timeout, or circuit-breaker middleware with `options.AddX402ApiHttpClients(..., builder => builder.AddRetryPolicy(...))`. Preserve the same idempotency key and body when retrying a mutation. HTTP error responses are returned as typed response wrappers; transport and cancellation failures throw exceptions. `*OrDefaultAsync` variants return `null` when a response cannot be mapped to their documented success result.

## API interfaces and functions

All methods are asynchronous and also have an `OrDefaultAsync` variant. Links lead to generated parameter, response, and status-code documentation.

| API interface | Function | HTTP endpoint |
| --- | --- | --- |
| [`IProgrammaticChargesApi`](docs/apis/ProgrammaticChargesApi.md) | `ChargesCreateAsync(idempotencyKey, dynamicChargeCreate)` | `POST /v1/charges` |
| [`IProgrammaticChargesApi`](docs/apis/ProgrammaticChargesApi.md) | `ChargesRetrieveAsync(chargeId)` | `GET /v1/charges/{charge_id}` |
| [`IFacilitatorDiscoveryApi`](docs/apis/FacilitatorDiscoveryApi.md) | `FacilitatorGetSupportedAsync()` | `GET /v1/facilitator/supported` |
| [`IIdempotencyApi`](docs/apis/IdempotencyApi.md) | `IdempotencyGetOutcomeAsync(idempotencyKey)` | `GET /v1/idempotency-outcomes/{idempotency_key}` |
| [`IResourcesAndPricingApi`](docs/apis/ResourcesAndPricingApi.md) | `NetworkFeesCreateQuoteAsync(networkFeePreview)` | `POST /v1/network-fee-quotes` |
| [`IOrdersAndPaymentsApi`](docs/apis/OrdersAndPaymentsApi.md) | `OrdersListAsync(cursor, pageSize)` | `GET /v1/orders` |
| [`IOrdersAndPaymentsApi`](docs/apis/OrdersAndPaymentsApi.md) | `OrdersRetrieveAsync(id)` | `GET /v1/orders/{id}` |
| [`IAssetsAndPaymentControlsApi`](docs/apis/AssetsAndPaymentControlsApi.md) | `PaymentReadinessRetrieveAsync()` | `GET /v1/payment-readiness` |
| [`IOrdersAndPaymentsApi`](docs/apis/OrdersAndPaymentsApi.md) | `PaymentsListAsync(cursor, pageSize)` | `GET /v1/payments` |
| [`IOrdersAndPaymentsApi`](docs/apis/OrdersAndPaymentsApi.md) | `PaymentsRetrieveAsync(id)` | `GET /v1/payments/{id}` |
| [`IOrdersAndPaymentsApi`](docs/apis/OrdersAndPaymentsApi.md) | `PaymentsListObservationsAsync(id, cursor, pageSize)` | `GET /v1/payments/{id}/observations` |
| [`IOrdersAndPaymentsApi`](docs/apis/OrdersAndPaymentsApi.md) | `PaymentsRetrieveReceiptAsync(id)` | `GET /v1/payments/{id}/receipt` |
| [`IOrdersAndPaymentsApi`](docs/apis/OrdersAndPaymentsApi.md) | `ReceiptVerificationKeysRetrieveAsync()` | `GET /v1/payment-receipt-verification-keys` |
| [`IReceivingAddressesApi`](docs/apis/ReceivingAddressesApi.md) | `ReceivingAddressesGetControlCapabilitiesAsync()` | `GET /v1/receiving-address-control-capabilities` |
| [`IReceivingAddressesApi`](docs/apis/ReceivingAddressesApi.md) | `ReceivingAddressesListAsync(cursor, pageSize)` | `GET /v1/receiving-addresses` |
| [`IResourcesAndPricingApi`](docs/apis/ResourcesAndPricingApi.md) | `ResourcesListAsync(cursor, pageSize)` | `GET /v1/resources` |
| [`IResourcesAndPricingApi`](docs/apis/ResourcesAndPricingApi.md) | `ResourcesCreateAsync(idempotencyKey, resourceCreate)` | `POST /v1/resources` |
| [`IResourcesAndPricingApi`](docs/apis/ResourcesAndPricingApi.md) | `ResourcesListVersionsAsync(resourceId, cursor, pageSize)` | `GET /v1/resources/{resource_id}/versions` |
| [`IResourcesAndPricingApi`](docs/apis/ResourcesAndPricingApi.md) | `ResourcesCreateVersionAsync(idempotencyKey, resourceId, body)` | `POST /v1/resources/{resource_id}/versions` |
| [`IWalletsAndTransfersApi`](docs/apis/WalletsAndTransfersApi.md) | `WalletsRetrieveBalanceAsync(id, finality)` | `GET /v1/wallets/{id}/balances` |

All request and response model documentation is in [`docs/models/`](docs/models/). See [`USAGE.md`](USAGE.md) for more complete patterns.

## Automatic generation

This repository uses OpenAPI Generator 7.24.0, pinned by Docker image and digest in [`scripts/generate-sdk.sh`](scripts/generate-sdk.sh). The [`SDK generation workflow`](.github/workflows/sdk_generation.yaml) checks the live OpenAPI document hourly and on manual or repository dispatch. When its normalized contract changes, GitHub Actions regenerates, validates, and commits the SDK to `main`.

To regenerate and validate locally with Docker and .NET 8:

```bash
./scripts/generate-sdk.sh
dotnet restore X402Api.sln
dotnet build X402Api.sln --configuration Release
```

Persistent files such as this README, `USAGE.md`, workflow configuration, and generator scripts are protected by [`.openapi-generator-ignore`](.openapi-generator-ignore). Generated client and model files should not be edited manually.

Licensed under the [MIT License](LICENSE).
