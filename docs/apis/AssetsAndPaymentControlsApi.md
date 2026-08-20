# X402Api.Api.AssetsAndPaymentControlsApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**PaymentReadinessRetrieve**](AssetsAndPaymentControlsApi.md#paymentreadinessretrieve) | **GET** /v1/payment-readiness | Retrieve payment readiness |

<a id="paymentreadinessretrieve"></a>
# **PaymentReadinessRetrieve**
> PaymentReadiness PaymentReadinessRetrieve ()

Retrieve payment readiness

Return the tenant's current external-wallet payment-readiness projection.


### Parameters
This endpoint does not need any parameter.
### Return type

[**PaymentReadiness**](PaymentReadiness.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for retrieve payment readiness. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
