# X402Api.Api.ProgrammaticChargesApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CreateDynamicCharge**](ProgrammaticChargesApi.md#createdynamiccharge) | **POST** /v1/charges |  |
| [**RetrieveDynamicCharge**](ProgrammaticChargesApi.md#retrievedynamiccharge) | **GET** /v1/charges/{charge_id} |  |

<a id="createdynamiccharge"></a>
# **CreateDynamicCharge**
> DynamicChargeResponse CreateDynamicCharge (string idempotencyKey, DynamicChargeCreate dynamicChargeCreate)



Create one idempotent dynamic charge from an active resource template. The immutable challenge freezes exact requested atomic amounts, eligible rails, verified tenant receiving addresses, fee policy and evidence, metadata, and expiry. The caller cannot supply a recipient address.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
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
| **201** |  |  -  |
| **409** |  |  -  |
| **422** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="retrievedynamiccharge"></a>
# **RetrieveDynamicCharge**
> DynamicChargeResponse RetrieveDynamicCharge (Guid chargeId)



Return the tenant-scoped frozen charge terms and current projected status without recomputing prices, recipients, rails, or fee evidence.


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
| **200** |  |  -  |
| **404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
