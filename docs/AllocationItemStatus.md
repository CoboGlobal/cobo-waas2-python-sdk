# AllocationItemStatus

The current status of the allocation item. - `Pending`: The allocation item has been created and recorded in the ledger. The system is determining whether further action is required. - `Transferring`: The on-chain transaction for the allocation item is in progress. - `Completed`: The allocation item is completed. Ledger-only allocation items are completed immediately, while on-chain allocation items are completed after the transfer succeeds. - `Failed`: The on-chain transfer failed or was rejected, including rejections caused by screening. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


