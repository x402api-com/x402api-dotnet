# X402Api.Model.DynamicChargeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChargeId** | **Guid** |  |
**ChargeDigest** | **string** |  |
**OrderId** | **Guid** |  |
**Status** | **string** |  |
**ResourceVersionId** | **Guid** |  |
**PaymentIdentifier** | **string** |  |
**ExpiresAt** | **DateTimeOffset** |  |
**CreatedAt** | **DateTimeOffset** |  |
**Prices** | [**List&lt;DynamicChargePrice&gt;**](DynamicChargePrice.md) |  |
**RequestedExpiresInSeconds** | **int** |  |
**Metadata** | **Dictionary&lt;string, Object&gt;** | Tenant application metadata frozen into the charge digest. Maximum canonical size is 16 KiB; floating-point numbers are not accepted. |
**MetadataDigest** | **string** |  |
**PaymentRequiredHeader** | **string** |  |
**EligibleAlternatives** | [**List&lt;NetworkFeeAlternative&gt;**](NetworkFeeAlternative.md) |  |
**FeePolicy** | [**FeePolicyDocument**](FeePolicyDocument.md) |  |
**FeeQuoteDigest** | **string** |  |
**PaymentRequired** | **Object** |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
