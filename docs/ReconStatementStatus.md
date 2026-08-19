# ReconStatementStatus

The reconciliation status of this daily statement row, captured **at the moment the day was closed**. Possible values include:   - `Confirmed`: All addresses of this wallet and token were reconciled against on-chain balances, so the figures in this row are trustworthy.   - `Halted`: At least one address failed the on-chain balance check, so reconciliation stopped there and the figures in this row may be incomplete or inaccurate.  Note this is a snapshot, not a live status: once a halted address is fixed, the row keeps reporting `Halted` until the day is reprocessed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


