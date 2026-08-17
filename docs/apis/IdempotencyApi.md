# X402Api.Api.IdempotencyApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**V1IdempotencyOutcomesRetrieve**](IdempotencyApi.md#v1idempotencyoutcomesretrieve) | **GET** /v1/idempotency-outcomes/{idempotency_key} |  |

<a id="v1idempotencyoutcomesretrieve"></a>
# **V1IdempotencyOutcomesRetrieve**
> IdempotencyOutcome V1IdempotencyOutcomesRetrieve (string idempotencyKey)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
