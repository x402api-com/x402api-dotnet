# X402Api.Model.NetworkFeeEvidence
Published shape for available and explicitly unavailable fee evidence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  |
**VarVersion** | **int** |  |
**Network** | **string** |  |
**AssetId** | **string** |  |
**PayloadProfile** | **string** |  |
**NativeSymbol** | **string** |  | [optional]
**NativeDecimals** | **int** |  | [optional]
**NativeFeeObservations** | [**List&lt;NativeFeeObservationEvidence&gt;**](NativeFeeObservationEvidence.md) |  | [optional]
**NativeUsdObservations** | [**List&lt;NativeUsdObservationEvidence&gt;**](NativeUsdObservationEvidence.md) |  | [optional]
**ExpiresAt** | **DateTimeOffset** |  | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
