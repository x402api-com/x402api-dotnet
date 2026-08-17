# X402Api.Api.ReceivingAddressesApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**V1ReceivingAddressControlCapabilitiesRetrieve**](ReceivingAddressesApi.md#v1receivingaddresscontrolcapabilitiesretrieve) | **GET** /v1/receiving-address-control-capabilities |  |
| [**V1ReceivingAddressControlChallengesCreate**](ReceivingAddressesApi.md#v1receivingaddresscontrolchallengescreate) | **POST** /v1/receiving-address-control-challenges |  |
| [**V1ReceivingAddressesActivateCreate**](ReceivingAddressesApi.md#v1receivingaddressesactivatecreate) | **POST** /v1/receiving-addresses/{readiness_id}/activate |  |
| [**V1ReceivingAddressesCreate**](ReceivingAddressesApi.md#v1receivingaddressescreate) | **POST** /v1/receiving-addresses |  |
| [**V1ReceivingAddressesList**](ReceivingAddressesApi.md#v1receivingaddresseslist) | **GET** /v1/receiving-addresses |  |
| [**V1ReceivingAddressesReadinessRefreshesCreate**](ReceivingAddressesApi.md#v1receivingaddressesreadinessrefreshescreate) | **POST** /v1/receiving-addresses/{readiness_id}/readiness-refreshes |  |
| [**V1ReceivingAddressesRotationsCreate**](ReceivingAddressesApi.md#v1receivingaddressesrotationscreate) | **POST** /v1/receiving-addresses/{readiness_id}/rotations |  |

<a id="v1receivingaddresscontrolcapabilitiesretrieve"></a>
# **V1ReceivingAddressControlCapabilitiesRetrieve**
> ExternalAddressControlCapabilities V1ReceivingAddressControlCapabilitiesRetrieve ()




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1receivingaddresscontrolchallengescreate"></a>
# **V1ReceivingAddressControlChallengesCreate**
> ExternalAddressControlChallenge V1ReceivingAddressControlChallengesCreate (string idempotencyKey, ExternalAddressControlChallengeCreate externalAddressControlChallengeCreate)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
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
| **201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1receivingaddressesactivatecreate"></a>
# **V1ReceivingAddressesActivateCreate**
> ExternalReceivingAddress V1ReceivingAddressesActivateCreate (string idempotencyKey, Guid readinessId)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1receivingaddressescreate"></a>
# **V1ReceivingAddressesCreate**
> ExternalReceivingAddress V1ReceivingAddressesCreate (string idempotencyKey, ExternalReceivingAddressCreate externalReceivingAddressCreate)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
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
| **201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1receivingaddresseslist"></a>
# **V1ReceivingAddressesList**
> List&lt;ExternalReceivingAddress&gt; V1ReceivingAddressesList (string cursor = null, int pageSize = null)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1receivingaddressesreadinessrefreshescreate"></a>
# **V1ReceivingAddressesReadinessRefreshesCreate**
> ExternalReceivingAddress V1ReceivingAddressesReadinessRefreshesCreate (string idempotencyKey, Guid readinessId)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
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
| **200** |  |  -  |
| **201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1receivingaddressesrotationscreate"></a>
# **V1ReceivingAddressesRotationsCreate**
> ExternalReceivingAddress V1ReceivingAddressesRotationsCreate (string idempotencyKey, Guid readinessId, ExternalReceivingAddressRotation externalReceivingAddressRotation)




### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | Unique mutation key; replaying different content returns HTTP 409. |  |
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
| **201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
