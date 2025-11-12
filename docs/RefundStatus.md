# RefundStatus

The current status of the refund order. For information about transaction status, see [Transaction statuses and sub-statuses](https://www.cobo.com/developers/v2/guides/transactions/status).  - `AddressPending`: The refund link has been created and opened but the address is not yet submitted. - `AddressSubmitted`: The address of the refund link has been submitted. - `Pending`: The refund order has been created but the transaction has not been initiated. - `Processing`: The refund order is currently being processed, with at least one refund transaction in progress. - `Completed`: All refund transactions have been completed successfully. - `PartiallyCompleted`: Some refund transactions have been completed successfully, while others have failed. - `Failed`: All refund transactions have failed. - `PendingConfirmation`: The refund order has been created but the address to send (`to_address`) has not been specified. Once you use the [Update refund order](https://www.cobo.com/developers/v2/api-references/payment/update-refund-order) operation to specify the address, the status will be updated to `Pending`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


