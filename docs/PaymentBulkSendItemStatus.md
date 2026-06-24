# PaymentBulkSendItemStatus

The current status of the bulk send item. Possible values include: - `Pending`: The bulk send item has been created and is waiting to be processed. - `Processing`: The bulk send item is currently being processed and the transfer is in progress. - `Completed`: The bulk send item has been successfully processed and the funds have been transferred. - `Failed`: The bulk send item was submitted for on-chain transfer, but the transfer attempt failed (for example, the batch payout could not be created, or the payout transaction failed, was rejected, or timed out). A transfer was attempted but the funds were not delivered; the locked amount is released and the commission fee is refunded. This is a terminal state. Resubmit the item to retry. - `NotExecuted`: The bulk send item was never submitted for on-chain transfer; it was skipped before any attempt. This happens when the item fails pre-execution (address or compliance) validation; or, in `Strict` execution mode, when any other item in the batch fails validation (in `Strict` mode all items become `NotExecuted` if one fails); or when an upstream step (fund sweep or commission fee charge) fails. No funds were moved and the locked amount is released. This is a terminal state. Fix the issue and resubmit the item to retry. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


