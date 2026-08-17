# X402Api.Api.ProgrammaticChargesApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ChargesCreate**](ProgrammaticChargesApi.md#chargescreate) | **POST** /v1/charges | Create a programmatic charge |
| [**ChargesRetrieve**](ProgrammaticChargesApi.md#chargesretrieve) | **GET** /v1/charges/{charge_id} | Retrieve a programmatic charge |

<a id="chargescreate"></a>
# **ChargesCreate**
> DynamicChargeResponse ChargesCreate (string idempotencyKey, DynamicChargeCreate dynamicChargeCreate)

Create a programmatic charge

Create one idempotent dynamic charge with immutable x402 payment terms.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
| **dynamicChargeCreate** | [**DynamicChargeCreate**](DynamicChargeCreate.md) |  |  |

### Return type

[**DynamicChargeResponse**](DynamicChargeResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response for create a programmatic charge. |  * X-Request-ID -  <br>  |
| **409** | The request failed. |  * X-Request-ID -  <br>  |
| **422** | The request failed. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="chargesretrieve"></a>
# **ChargesRetrieve**
> DynamicChargeResponse ChargesRetrieve (Guid chargeId)

Retrieve a programmatic charge

Retrieve the frozen terms and current projected status of a tenant charge.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **chargeId** | **Guid** |  |  |

### Return type

[**DynamicChargeResponse**](DynamicChargeResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for retrieve a programmatic charge. |  * X-Request-ID -  <br>  |
| **404** | The request failed. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
