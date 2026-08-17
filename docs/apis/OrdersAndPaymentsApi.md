# X402Api.Api.OrdersAndPaymentsApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**V1OrdersList**](OrdersAndPaymentsApi.md#v1orderslist) | **GET** /v1/orders |  |
| [**V1OrdersRetrieve**](OrdersAndPaymentsApi.md#v1ordersretrieve) | **GET** /v1/orders/{id} |  |
| [**V1PaymentReceiptVerificationKeysRetrieve**](OrdersAndPaymentsApi.md#v1paymentreceiptverificationkeysretrieve) | **GET** /v1/payment-receipt-verification-keys |  |
| [**V1PaymentsList**](OrdersAndPaymentsApi.md#v1paymentslist) | **GET** /v1/payments |  |
| [**V1PaymentsObservationsList**](OrdersAndPaymentsApi.md#v1paymentsobservationslist) | **GET** /v1/payments/{id}/observations |  |
| [**V1PaymentsReceiptRetrieve**](OrdersAndPaymentsApi.md#v1paymentsreceiptretrieve) | **GET** /v1/payments/{id}/receipt |  |
| [**V1PaymentsRetrieve**](OrdersAndPaymentsApi.md#v1paymentsretrieve) | **GET** /v1/payments/{id} |  |

<a id="v1orderslist"></a>
# **V1OrdersList**
> List&lt;Order&gt; V1OrdersList (string cursor = null, int pageSize = null)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1ordersretrieve"></a>
# **V1OrdersRetrieve**
> Order V1OrdersRetrieve (Guid id)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1paymentreceiptverificationkeysretrieve"></a>
# **V1PaymentReceiptVerificationKeysRetrieve**
> ReceiptVerificationKeyHistory V1PaymentReceiptVerificationKeysRetrieve ()



Public key history; authenticity still requires an out-of-band pin.


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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1paymentslist"></a>
# **V1PaymentsList**
> List&lt;SettlementJob&gt; V1PaymentsList (string cursor = null, int pageSize = null)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1paymentsobservationslist"></a>
# **V1PaymentsObservationsList**
> List&lt;SettlementChainObservation&gt; V1PaymentsObservationsList (Guid id, string cursor = null, int pageSize = null)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1paymentsreceiptretrieve"></a>
# **V1PaymentsReceiptRetrieve**
> PaymentReceipt V1PaymentsReceiptRetrieve (Guid id)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="v1paymentsretrieve"></a>
# **V1PaymentsRetrieve**
> SettlementJob V1PaymentsRetrieve (Guid id)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
