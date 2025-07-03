# RefundStatus

The current status of the refund order. For information about transaction status, see [Transaction statuses and sub-statuses](https://www.cobo.com/developers/v2/guides/transactions/status).  - `Pending`: The refund order has been created but the transaction has not been initiated. - `Processing`: The refund order is currently being processed, with at least one refund transaction in progress. - `Completed`: All refund transactions have been completed successfully. - `PartiallyCompleted`: Some refund transactions have been completed successfully, while others have failed. - `Failed`: All refund transactions have failed. - `PendingConfirmation`: The refund order has been completed but the address to send is pending confirmation. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


