# WebhookEventStatus

The event status. Possible values include: - `Success`: The event has been delivered, and the webhook endpoint has responded to the event. - `Retrying`: The event has been delivered, but the webhook endpoint has not responded. In this case, Cobo will retry delivering the event. - `Failed`: The event cannot be delivered and Cobo will stop retrying. This may occur if the number of retries reaches 10, or if the event has been delivered but the webhook endpoint responded with an error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


