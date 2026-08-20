# X402Api.Model.WalletBalanceResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WalletId** | **Guid** |  |
**Network** | **string** |  |
**RequestedFinality** | **WalletObservationFinalityEnum** |  |
**ObservationState** | **ObservationStateEnum** |  |
**TrackingStatus** | **TrackingStatusEnum** |  |
**Assets** | [**List&lt;BalanceAsset&gt;**](BalanceAsset.md) |  |
**WalletVersions** | [**List&lt;WalletVersionBalance&gt;**](WalletVersionBalance.md) |  |
**ReseedContexts** | [**List&lt;WalletFencedChainReseedContext&gt;**](WalletFencedChainReseedContext.md) |  |
**WalletAddress** | **string** |  |
**ObservedAt** | **DateTimeOffset** |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
