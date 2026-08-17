# X402Api.Api.ReceivingAddressesApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ReceivingAddressesActivate**](ReceivingAddressesApi.md#receivingaddressesactivate) | **POST** /v1/receiving-addresses/{readiness_id}/activate | Activate a receiving address |
| [**ReceivingAddressesCreateControlChallenge**](ReceivingAddressesApi.md#receivingaddressescreatecontrolchallenge) | **POST** /v1/receiving-address-control-challenges | Create a receiving-address control challenge |
| [**ReceivingAddressesGetControlCapabilities**](ReceivingAddressesApi.md#receivingaddressesgetcontrolcapabilities) | **GET** /v1/receiving-address-control-capabilities | Get receiving-address control capabilities |
| [**ReceivingAddressesList**](ReceivingAddressesApi.md#receivingaddresseslist) | **GET** /v1/receiving-addresses | List receiving addresses |
| [**ReceivingAddressesRefreshReadiness**](ReceivingAddressesApi.md#receivingaddressesrefreshreadiness) | **POST** /v1/receiving-addresses/{readiness_id}/readiness-refreshes | Refresh receiving-address readiness |
| [**ReceivingAddressesRegister**](ReceivingAddressesApi.md#receivingaddressesregister) | **POST** /v1/receiving-addresses | Register a receiving address |
| [**ReceivingAddressesRotate**](ReceivingAddressesApi.md#receivingaddressesrotate) | **POST** /v1/receiving-addresses/{readiness_id}/rotations | Rotate a receiving address |

<a id="receivingaddressesactivate"></a>
# **ReceivingAddressesActivate**
> ExternalReceivingAddress ReceivingAddressesActivate (string idempotencyKey, Guid readinessId)

Activate a receiving address

Activate a ready external receiving-address registration idempotently.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
| **readinessId** | **Guid** |  |  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for activate a receiving address. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="receivingaddressescreatecontrolchallenge"></a>
# **ReceivingAddressesCreateControlChallenge**
> ExternalAddressControlChallenge ReceivingAddressesCreateControlChallenge (string idempotencyKey, ExternalAddressControlChallengeCreate externalAddressControlChallengeCreate)

Create a receiving-address control challenge

Create an idempotent proof-of-control challenge for an external receiving address.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
| **externalAddressControlChallengeCreate** | [**ExternalAddressControlChallengeCreate**](ExternalAddressControlChallengeCreate.md) |  |  |

### Return type

[**ExternalAddressControlChallenge**](ExternalAddressControlChallenge.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response for create a receiving-address control challenge. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="receivingaddressesgetcontrolcapabilities"></a>
# **ReceivingAddressesGetControlCapabilities**
> ExternalAddressControlCapabilities ReceivingAddressesGetControlCapabilities ()

Get receiving-address control capabilities

Return the supported proof and control capabilities for external receiving addresses.


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

List tenant receiving-address registrations using opaque cursor pagination.


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

<a id="receivingaddressesrefreshreadiness"></a>
# **ReceivingAddressesRefreshReadiness**
> ExternalReceivingAddress ReceivingAddressesRefreshReadiness (string idempotencyKey, Guid readinessId)

Refresh receiving-address readiness

Request an idempotent refresh of external receiving-address readiness evidence.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
| **readinessId** | **Guid** |  |  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for refresh receiving-address readiness. |  * X-Request-ID -  <br>  |
| **201** | Successful response for refresh receiving-address readiness. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="receivingaddressesregister"></a>
# **ReceivingAddressesRegister**
> ExternalReceivingAddress ReceivingAddressesRegister (string idempotencyKey, ExternalReceivingAddressCreate externalReceivingAddressCreate)

Register a receiving address

Register a proven external receiving address without transferring wallet custody.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
| **externalReceivingAddressCreate** | [**ExternalReceivingAddressCreate**](ExternalReceivingAddressCreate.md) |  |  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response for register a receiving address. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="receivingaddressesrotate"></a>
# **ReceivingAddressesRotate**
> ExternalReceivingAddress ReceivingAddressesRotate (string idempotencyKey, Guid readinessId, ExternalReceivingAddressRotation externalReceivingAddressRotation)

Rotate a receiving address

Create an idempotent receiving-address rotation from a proven replacement.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Caller-persisted mutation key containing 8 to 160 safe ASCII characters. Replay the exact key and body after an uncertain outcome. |  |
| **readinessId** | **Guid** |  |  |
| **externalReceivingAddressRotation** | [**ExternalReceivingAddressRotation**](ExternalReceivingAddressRotation.md) |  |  |

### Return type

[**ExternalReceivingAddress**](ExternalReceivingAddress.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response for rotate a receiving address. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
