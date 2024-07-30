# WebhookEndpointStatus

The webhook endpoint status. Possible values include: - `STATUS_ACTIVE`: The endpoint is currently in use. - `STATUS_INACTIVE`: The endpoint has been revoked and can no longer receive webhook events. - `STATUS_PENDING_ACTIVE`: The request to create the endpoint is awaiting approval. After the approval, the endpoint will be available for use. - `STATUS_PENDING_INACTIVE`: The request to revoke the endpoint is awaiting approval. After the approval,the endpoint will no longer receive webhook events. - `STATUS_PENDING_UPDATE`: The request to update the endpoint is awaiting approval. After the approval, the endpoint will be updated. - `STATUS_REJECT_ACTIVE`: The request to create the endpoint has been rejected. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


