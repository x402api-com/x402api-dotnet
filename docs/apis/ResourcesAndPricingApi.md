# X402Api.Api.ResourcesAndPricingApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**NetworkFeesCreateQuote**](ResourcesAndPricingApi.md#networkfeescreatequote) | **POST** /v1/network-fee-quotes | Create a network-fee quote |
| [**ResourcesCreate**](ResourcesAndPricingApi.md#resourcescreate) | **POST** /v1/resources | Create a resource |
| [**ResourcesCreateVersion**](ResourcesAndPricingApi.md#resourcescreateversion) | **POST** /v1/resources/{resource_id}/versions | Create a resource version |
| [**ResourcesList**](ResourcesAndPricingApi.md#resourceslist) | **GET** /v1/resources | List resources |
| [**ResourcesListVersions**](ResourcesAndPricingApi.md#resourceslistversions) | **GET** /v1/resources/{resource_id}/versions | List resource versions |

<a id="networkfeescreatequote"></a>
# **NetworkFeesCreateQuote**
> NetworkFeePreviewResponse NetworkFeesCreateQuote (NetworkFeePreview networkFeePreview)

Create a network-fee quote

Preview bounded network fees for the requested resource prices and rails. Requires a tenant API key with the `resources:read` scope.


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
| **200** | Successful response for create a network-fee quote. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="resourcescreate"></a>
# **ResourcesCreate**
> Resource ResourcesCreate (string idempotencyKey, ResourceCreate resourceCreate)

Create a resource

Create one tenant resource idempotently. Requires a tenant API key with the `resources:write` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
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
| **201** | Successful response for create a resource. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="resourcescreateversion"></a>
# **ResourcesCreateVersion**
> ResourceVersion ResourcesCreateVersion (string idempotencyKey, Guid resourceId, ResourceVersionCreate resourceVersionCreate)

Create a resource version

Create an immutable priced version of one tenant resource idempotently. Requires a tenant API key with the `resources:write` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
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
| **201** | Successful response for create a resource version. |  * X-Request-ID -  <br>  |
| **409** | The request failed. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="resourceslist"></a>
# **ResourcesList**
> List&lt;Resource&gt; ResourcesList (string cursor = null, int pageSize = null)

List resources

List tenant resources and their visible versions using opaque cursor pagination. Requires a tenant API key with the `resources:read` scope.


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
| **200** | Successful response for list resources. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="resourceslistversions"></a>
# **ResourcesListVersions**
> List&lt;ResourceVersion&gt; ResourcesListVersions (Guid resourceId, string cursor = null, int pageSize = null)

List resource versions

List immutable versions of one tenant resource using opaque cursor pagination. Requires a tenant API key with the `resources:read` scope.


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
| **200** | Successful response for list resource versions. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
