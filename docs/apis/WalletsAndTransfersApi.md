# X402Api.Api.WalletsAndTransfersApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**WalletsRetrieveBalance**](WalletsAndTransfersApi.md#walletsretrievebalance) | **GET** /v1/wallets/{id}/balances | Retrieve wallet balances |

<a id="walletsretrievebalance"></a>
# **WalletsRetrieveBalance**
> WalletBalanceResponse WalletsRetrieveBalance (Guid id, string finality = null)

Retrieve wallet balances

Retrieve finalized external-wallet balance observations at the requested finality. Requires a tenant API key with the `balances:read` scope.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** |  |  |
| **finality** | **string** |  | [optional] [default to finalized] |

### Return type

[**WalletBalanceResponse**](WalletBalanceResponse.md)

### Authorization

[tenantApiKey](../README.md#tenantApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response for retrieve wallet balances. |  * X-Request-ID -  <br>  |
| **0** | The request failed with a stable machine-readable error. |  * X-Request-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
