# PaymentPayoutStatus

The current status of the payout. Possible values include: - `Pending`: The payout has been created and is awaiting processing. - `Preparing`: The payout is being prepared for transfer. - `Transferring`: The payout is currently being transferred to the recipient's destination. - `Completed`: The payout has been successfully completed and all transactions have been processed. - `PartiallyCompleted`: The payout has been partially completed, with some transactions succeeding and others failing. - `Failed`: The payout has failed and no transactions were completed successfully. - `RejectedByBank`: The payout was rejected by the recipient's bank (applicable to OffRamp payouts only). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


