# X402Api.Api.FacilitatorDiscoveryApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**FacilitatorGetSupported**](FacilitatorDiscoveryApi.md#facilitatorgetsupported) | **GET** /v1/facilitator/supported | Get supported facilitator profiles |

<a id="facilitatorgetsupported"></a>
# **FacilitatorGetSupported**
> SupportedResponse FacilitatorGetSupported ()

Get supported facilitator profiles

Return the currently approved public x402 facilitator profiles.


### Parameters
This endpoint does not need any parameter.
### Return type

[**SupportedResponse**](SupportedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for get supported facilitator profiles. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
