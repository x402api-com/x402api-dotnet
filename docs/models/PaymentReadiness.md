# X402Api.Model.PaymentReadiness

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**State** | **PaymentReadinessStateEnum** |  | [readonly]
**AcceptingNewPayments** | **bool** |  | [readonly]
**ReadyForNewPayment** | **bool** |  | [readonly]
**PausedByTenant** | **bool** |  | [readonly]
**PlatformAvailable** | **bool** |  | [readonly]
**ObservedAt** | **DateTimeOffset** |  | [readonly]
**TenantStatus** | **string** |  | [readonly]
**TenantAcceptingNewChallenges** | **bool** |  | [readonly]
**GlobalChallengesEnabled** | **bool** |  | [readonly]
**GlobalSettlementEnabled** | **bool** |  | [readonly]
**ControlPlaneReadyForNewChallenges** | **bool** |  | [readonly]
**ControlPlaneReadyForSettlement** | **bool** |  | [readonly]
**Rails** | [**List&lt;PaymentReadinessRail&gt;**](PaymentReadinessRail.md) |  | [readonly]
**CanonicalRails** | [**List&lt;CanonicalPaymentReadinessRail&gt;**](CanonicalPaymentReadinessRail.md) |  | [readonly]
**HealthValidUntil** | **DateTimeOffset** |  | [readonly]
**ExternalOnboarding** | **Object** |  | [readonly]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
