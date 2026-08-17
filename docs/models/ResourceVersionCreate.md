# X402Api.Model.ResourceVersionCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExpectedLatestVersion** | **int** |  |
**Method** | **HTTPMethodEnum** |  |
**Path** | **string** |  |
**Description** | **string** |  |
**FulfillmentMode** | **ResourceInputFulfillmentModeEnum** |  |
**Prices** | [**List&lt;PriceInput&gt;**](PriceInput.md) |  |
**FeeMode** | **FeePolicyModeInputEnum** |  | [optional]
**QuoteCurrency** | **FeePolicyQuoteCurrencyInputEnum** |  | [optional]
**FeeAllowanceCapQuoteMicros** | **string** |  | [optional] [default to "0"]
**MimeType** | **string** |  | [optional] [default to "application/json"]
**FulfillmentConfig** | [**ResourceCreateFulfillmentConfig**](ResourceCreateFulfillmentConfig.md) |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
