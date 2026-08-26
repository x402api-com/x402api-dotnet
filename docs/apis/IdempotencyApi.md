# X402Api.Api.IdempotencyApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**IdempotencyGetOutcome**](IdempotencyApi.md#idempotencygetoutcome) | **GET** /v1/idempotency-outcomes/{idempotency_key} | Get an idempotency outcome |

<a id="idempotencygetoutcome"></a>
# **IdempotencyGetOutcome**
> IdempotencyOutcome IdempotencyGetOutcome (string idempotencyKey)

Get an idempotency outcome

Return the authoritative tenant-scoped outcome for a durable mutation key. Requires an authenticated tenant API key; no additional scope is required.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** |  |  |

### Return type

[**IdempotencyOutcome**](IdempotencyOutcome.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for get an idempotency outcome. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
