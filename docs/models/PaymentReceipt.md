# X402Api.Model.PaymentReceipt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | [readonly]
**OrderId** | **Guid** |  | [readonly]
**SettlementJobId** | **Guid** |  | [readonly]
**ReceiptDigest** | **string** |  | [readonly]
**Signature** | **string** |  | [readonly]
**SigningKeyVersion** | **string** |  | [readonly]
**EligibleAlternatives** | [**List&lt;PublicNetworkFeeAlternative&gt;**](PublicNetworkFeeAlternative.md) |  | [readonly]
**SettlementAmountAtomic** | **string** |  | [readonly]
**GasMode** | **string** |  | [readonly]
**CreatedAt** | **DateTimeOffset** |  | [readonly]
**Receipt** | **Object** |  | [readonly]
**FeePolicy** | [**PublicFeePolicyDocument**](PublicFeePolicyDocument.md) |  | [readonly]
**FeeEvidence** | **Dictionary&lt;string, Object&gt;** |  | [readonly]
**FeeQuoteDigest** | **string** |  | [readonly]
**FeeQuoteExpiresAt** | **DateTimeOffset** |  | [readonly]
**BuyerNativeFeeAtomic** | **string** |  | [readonly]
**SponsoredNativeFeeAtomic** | **string** |  | [readonly]
**SponsoredNativeSymbol** | **string** |  | [readonly]
**TenantGasChargeMicros** | **string** |  | [readonly]
**GasSponsorshipEvidenceDigest** | **string** |  | [readonly]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
