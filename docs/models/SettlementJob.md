# X402Api.Model.SettlementJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | [readonly]
**OrderId** | **Guid** |  | [readonly]
**ReservationId** | **Guid** |  | [readonly]
**State** | **SettlementJobStateEnum** |  | [readonly]
**Network** | **string** |  | [readonly]
**TransactionHash** | **string** |  | [readonly]
**OriginalTransactionHash** | **string** |  | [readonly]
**ReplacedByHash** | **string** |  | [readonly]
**GasExecutionState** | **string** |  | [readonly]
**GasExecutionSequence** | **int** |  | [readonly]
**GasExecutionMaterialDigest** | **string** |  | [readonly]
**Payer** | **string** |  | [readonly]
**LastErrorCode** | **string** |  | [readonly]
**BroadcastAttemptCount** | **int** |  | [readonly]
**CreatedAt** | **DateTimeOffset** |  | [readonly]
**UpdatedAt** | **DateTimeOffset** |  | [readonly]
**Order** | [**TenantPaymentOrderProjection**](TenantPaymentOrderProjection.md) |  | [readonly]
**Resource** | [**TenantPaymentResourceProjection**](TenantPaymentResourceProjection.md) |  | [readonly]
**Asset** | [**TenantPaymentAssetProjection**](TenantPaymentAssetProjection.md) |  | [readonly]
**Chain** | [**TenantPaymentChainProjection**](TenantPaymentChainProjection.md) |  | [readonly]
**Receipt** | [**TenantPaymentReceiptProjection**](TenantPaymentReceiptProjection.md) |  | [readonly]
**Screening** | [**TenantPaymentScreeningProjection**](TenantPaymentScreeningProjection.md) |  | [readonly]
**Fulfillment** | [**TenantPaymentFulfillmentProjection**](TenantPaymentFulfillmentProjection.md) |  | [readonly]
**GasExecutionObservedAt** | **DateTimeOffset** |  | [readonly]
**SettlementResult** | **Object** |  | [readonly]
**ConfirmedAt** | **DateTimeOffset** |  | [readonly]
**FinalizedAt** | **DateTimeOffset** |  | [readonly]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
