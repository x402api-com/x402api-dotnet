# X402Api.Api.ResourcesAndPricingApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**V1NetworkFeeQuotesCreate**](ResourcesAndPricingApi.md#v1networkfeequotescreate) | **POST** /v1/network-fee-quotes |  |
| [**V1ResourcesCreate**](ResourcesAndPricingApi.md#v1resourcescreate) | **POST** /v1/resources |  |
| [**V1ResourcesList**](ResourcesAndPricingApi.md#v1resourceslist) | **GET** /v1/resources |  |
| [**V1ResourcesVersionsActivateCreate**](ResourcesAndPricingApi.md#v1resourcesversionsactivatecreate) | **POST** /v1/resources/{resource_id}/versions/{version_id}/activate |  |
| [**V1ResourcesVersionsCreate**](ResourcesAndPricingApi.md#v1resourcesversionscreate) | **POST** /v1/resources/{resource_id}/versions |  |
| [**V1ResourcesVersionsList**](ResourcesAndPricingApi.md#v1resourcesversionslist) | **GET** /v1/resources/{resource_id}/versions |  |
| [**V1ResourcesVersionsRetireCreate**](ResourcesAndPricingApi.md#v1resourcesversionsretirecreate) | **POST** /v1/resources/{resource_id}/versions/{version_id}/retire |  |

<a id="v1networkfeequotescreate"></a>
# **V1NetworkFeeQuotesCreate**
> NetworkFeePreviewResponse V1NetworkFeeQuotesCreate (NetworkFeePreview networkFeePreview)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **networkFeePreview** | [**NetworkFeePreview**](NetworkFeePreview.md) |  |  |

### Return type

[**NetworkFeePreviewResponse**](NetworkFeePreviewResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1resourcescreate"></a>
# **V1ResourcesCreate**
> Resource V1ResourcesCreate (string idempotencyKey, ResourceCreate resourceCreate)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
| **resourceCreate** | [**ResourceCreate**](ResourceCreate.md) |  |  |

### Return type

[**Resource**](Resource.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1resourceslist"></a>
# **V1ResourcesList**
> List&lt;Resource&gt; V1ResourcesList (string cursor = null, int pageSize = null)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]  |
| **pageSize** | **int** | Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100] |

### Return type

[**List&lt;Resource&gt;**](Resource.md)

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

<a id="v1resourcesversionsactivatecreate"></a>
# **V1ResourcesVersionsActivateCreate**
> ResourceVersion V1ResourcesVersionsActivateCreate (string idempotencyKey, Guid resourceId, Guid versionId, ResourceVersionActivate resourceVersionActivate)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
| **resourceId** | **Guid** |  |  |
| **versionId** | **Guid** |  |  |
| **resourceVersionActivate** | [**ResourceVersionActivate**](ResourceVersionActivate.md) |  |  |

### Return type

[**ResourceVersion**](ResourceVersion.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1resourcesversionscreate"></a>
# **V1ResourcesVersionsCreate**
> ResourceVersion V1ResourcesVersionsCreate (string idempotencyKey, Guid resourceId, ResourceVersionCreate resourceVersionCreate)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
| **resourceId** | **Guid** |  |  |
| **resourceVersionCreate** | [**ResourceVersionCreate**](ResourceVersionCreate.md) |  |  |

### Return type

[**ResourceVersion**](ResourceVersion.md)

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

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1resourcesversionslist"></a>
# **V1ResourcesVersionsList**
> List&lt;ResourceVersion&gt; V1ResourcesVersionsList (Guid resourceId, string cursor = null, int pageSize = null)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **resourceId** | **Guid** |  |  |
| **cursor** | **string** | Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]  |
| **pageSize** | **int** | Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100] |

### Return type

[**List&lt;ResourceVersion&gt;**](ResourceVersion.md)

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

<a id="v1resourcesversionsretirecreate"></a>
# **V1ResourcesVersionsRetireCreate**
> ResourceVersion V1ResourcesVersionsRetireCreate (string idempotencyKey, Guid resourceId, Guid versionId, ResourceVersionRetire resourceVersionRetire)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
| **resourceId** | **Guid** |  |  |
| **versionId** | **Guid** |  |  |
| **resourceVersionRetire** | [**ResourceVersionRetire**](ResourceVersionRetire.md) |  |  |

### Return type

[**ResourceVersion**](ResourceVersion.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
