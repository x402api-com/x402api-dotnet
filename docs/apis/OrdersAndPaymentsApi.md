# X402Api.Api.OrdersAndPaymentsApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**OrdersList**](OrdersAndPaymentsApi.md#orderslist) | **GET** /v1/orders | List orders |
| [**OrdersRetrieve**](OrdersAndPaymentsApi.md#ordersretrieve) | **GET** /v1/orders/{id} | Retrieve an order |
| [**PaymentsList**](OrdersAndPaymentsApi.md#paymentslist) | **GET** /v1/payments | List payments |
| [**PaymentsListObservations**](OrdersAndPaymentsApi.md#paymentslistobservations) | **GET** /v1/payments/{id}/observations | List payment observations |
| [**PaymentsRetrieve**](OrdersAndPaymentsApi.md#paymentsretrieve) | **GET** /v1/payments/{id} | Retrieve a payment |
| [**PaymentsRetrieveReceipt**](OrdersAndPaymentsApi.md#paymentsretrievereceipt) | **GET** /v1/payments/{id}/receipt | Retrieve a payment receipt |
| [**ReceiptVerificationKeysRetrieve**](OrdersAndPaymentsApi.md#receiptverificationkeysretrieve) | **GET** /v1/payment-receipt-verification-keys | Retrieve receipt verification keys |

<a id="orderslist"></a>
# **OrdersList**
> List&lt;Order&gt; OrdersList (string cursor = null, int pageSize = null)

List orders

List tenant-visible orders using opaque cursor pagination. Requires a tenant API key with the `orders:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]  |
| **pageSize** | **int** | Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100] |

### Return type

[**List&lt;Order&gt;**](Order.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for list orders. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="ordersretrieve"></a>
# **OrdersRetrieve**
> Order OrdersRetrieve (Guid id)

Retrieve an order

Retrieve one tenant-visible order by its canonical identifier. Requires a tenant API key with the `orders:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

### Return type

[**Order**](Order.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for retrieve an order. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="paymentslist"></a>
# **PaymentsList**
> List&lt;SettlementJob&gt; PaymentsList (string cursor = null, int pageSize = null)

List payments

List tenant-visible payments using opaque cursor pagination. Requires a tenant API key with the `payments:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]  |
| **pageSize** | **int** | Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100] |

### Return type

[**List&lt;SettlementJob&gt;**](SettlementJob.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for list payments. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="paymentslistobservations"></a>
# **PaymentsListObservations**
> List&lt;SettlementChainObservation&gt; PaymentsListObservations (Guid id, string cursor = null, int pageSize = null)

List payment observations

List finalized and pending chain observations for one tenant-visible payment. Requires a tenant API key with the `payments:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **cursor** | **string** | Opaque pagination cursor from X-X402API-Next-Cursor or rel&#x3D;next Link. | [optional]  |
| **pageSize** | **int** | Number of results in the bounded array page (default and maximum 100). | [optional] [default to 100] |

### Return type

[**List&lt;SettlementChainObservation&gt;**](SettlementChainObservation.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for list payment observations. |  * X-Request-ID -  <br>  * Link -  <br>  * X-X402API-Next-Cursor -  <br>  * X-X402API-Result-Truncated -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="paymentsretrieve"></a>
# **PaymentsRetrieve**
> SettlementJob PaymentsRetrieve (Guid id)

Retrieve a payment

Retrieve one tenant-visible payment by its canonical identifier. Requires a tenant API key with the `payments:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

### Return type

[**SettlementJob**](SettlementJob.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for retrieve a payment. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="paymentsretrievereceipt"></a>
# **PaymentsRetrieveReceipt**
> PaymentReceipt PaymentsRetrieveReceipt (Guid id)

Retrieve a payment receipt

Retrieve the signed receipt projection for one tenant-visible payment. Requires a tenant API key with the `payments:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |

### Return type

[**PaymentReceipt**](PaymentReceipt.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for retrieve a payment receipt. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="receiptverificationkeysretrieve"></a>
# **ReceiptVerificationKeysRetrieve**
> ReceiptVerificationKeyHistory ReceiptVerificationKeysRetrieve ()

Retrieve receipt verification keys

Return the public receipt verification-key history for out-of-band-pinned verification. Public endpoint; no API key or scope is required.


### Parameters
This endpoint does not need any parameter.
### Return type

[**ReceiptVerificationKeyHistory**](ReceiptVerificationKeyHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for retrieve receipt verification keys. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
