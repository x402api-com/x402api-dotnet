# X402Api.Api.WalletsAndTransfersApi

All URIs are relative to *https://api.x402api.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**V1WalletsBalancesRetrieve**](WalletsAndTransfersApi.md#v1walletsbalancesretrieve) | **GET** /v1/wallets/{id}/balances |  |

<a id="v1walletsbalancesretrieve"></a>
# **V1WalletsBalancesRetrieve**
> WalletBalanceResponse V1WalletsBalancesRetrieve (Guid id, string finality = null)




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
| **200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)
