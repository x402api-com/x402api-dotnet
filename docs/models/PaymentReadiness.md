# X402Api.Model.PaymentReadiness

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ObservedAt** | **DateTimeOffset** |  | [readonly]
**TenantStatus** | **string** |  | [readonly]
**TenantAcceptingNewChallenges** | **bool** |  | [readonly]
**GlobalChallengesEnabled** | **bool** |  | [readonly]
**GlobalSettlementEnabled** | **bool** |  | [readonly]
**ControlPlaneReadyForNewChallenges** | **bool** |  | [readonly]
**ControlPlaneReadyForSettlement** | **bool** |  | [readonly]
**Rails** | [**List&lt;PaymentReadinessRail&gt;**](PaymentReadinessRail.md) |  | [readonly]
**ExternalOnboarding** | **Object** |  | [readonly]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
