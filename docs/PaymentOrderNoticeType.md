# PaymentOrderNoticeType

The reason an order update is sent when the order's primary status does not change: - `PaymentUpdated`: A related incoming transaction requires customer action. - `PaymentFailed`: A related incoming transaction failed and cannot be credited to the order. - `LatePaymentReceived`: An incoming transaction was completed after the order had already reached a terminal status. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


