# X402Api.Api.ReceivingAddressesApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ReceivingAddressesGetControlCapabilities**](ReceivingAddressesApi.md#receivingaddressesgetcontrolcapabilities) | **GET** /v1/receiving-address-control-capabilities | Get receiving-address control capabilities |
| [**ReceivingAddressesList**](ReceivingAddressesApi.md#receivingaddresseslist) | **GET** /v1/receiving-addresses | List receiving addresses |

<a id="receivingaddressesgetcontrolcapabilities"></a>
# **ReceivingAddressesGetControlCapabilities**
> ExternalAddressControlCapabilities ReceivingAddressesGetControlCapabilities ()

Get receiving-address control capabilities

Return the supported proof and control capabilities for external receiving addresses. Requires a tenant API key with the `wallets:read` scope.


### Parameters
This endpoint does not need any parameter.
### Return type

[**ExternalAddressControlCapabilities**](ExternalAddressControlCapabilities.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for get receiving-address control capabilities. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="receivingaddresseslist"></a>
# **ReceivingAddressesList**
> List&lt;ExternalReceivingAddress&gt; ReceivingAddressesList (string cursor = null, int pageSize = null)

List receiving addresses

List tenant receiving-address registrations using opaque cursor pagination. Requires a tenant API key with the `wallets:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]  |
| **pageSize** | **int** | Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100] |

### Return type

[**List&lt;ExternalReceivingAddress&gt;**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for list receiving addresses. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
