# X402Api.Model.DynamicChargeCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ResourceVersionId** | **Guid** |  |
**ResourceUrl** | **string** |  |
**Prices** | [**List&lt;DynamicChargePrice&gt;**](DynamicChargePrice.md) |  |
**ExpiresInSeconds** | **int** |  |
**Method** | **HTTPMethodEnum** |  | [optional]
**BodyBase64** | **string** |  | [optional] [default to ""]
**ContentType** | **string** |  | [optional]
**Description** | **string** |  | [optional]
**FeeMode** | **FeePolicyModeInputEnum** |  | [optional]
**QuoteCurrency** | **FeePolicyQuoteCurrencyInputEnum** |  | [optional]
**FeeAllowanceCapQuoteMicros** | **string** |  | [optional]
**Metadata** | **Dictionary&lt;string, Object&gt;** | Tenant application metadata frozen into the charge digest. Maximum canonical size is 16 KiB; floating-point numbers are not accepted. | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
