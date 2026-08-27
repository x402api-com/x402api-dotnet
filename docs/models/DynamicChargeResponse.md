# X402Api.Model.DynamicChargeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ChargeId** | **Guid** | Immutable challenge UUID created for this charge. |
**ChargeDigest** | **string** |  |
**OrderId** | **Guid** |  |
**Status** | **string** | Current projected order status; payment terms remain immutable. |
**ResourceVersionId** | **Guid** |  |
**PaymentIdentifier** | **string** | Opaque server challenge handle. Return it to the buyer as X-X402API-Challenge-Handle; it is not the buyer payment identifier. |
**ExpiresAt** | **DateTimeOffset** |  |
**CreatedAt** | **DateTimeOffset** |  |
**Prices** | [**List&lt;DynamicChargePrice&gt;**](DynamicChargePrice.md) |  |
**RequestedExpiresInSeconds** | **int** |  |
**Metadata** | **Dictionary&lt;string, Object&gt;** | Tenant application metadata frozen into the charge digest. Maximum canonical size is 16 KiB; floating-point numbers are not accepted. |
**MetadataDigest** | **string** |  |
**PaymentRequiredHeader** | **string** | Canonical base64-encoded value to return in the buyer-facing PAYMENT-REQUIRED header. |
**EligibleAlternatives** | [**List&lt;NetworkFeeAlternative&gt;**](NetworkFeeAlternative.md) |  |
**FeePolicy** | [**FeePolicyDocument**](FeePolicyDocument.md) |  |
**FeeQuoteDigest** | **string** |  |
**PaymentRequired** | **Object** | Complete immutable x402 v2 PAYMENT-REQUIRED document. |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
