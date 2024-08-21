# TSSRequestStatus

The TSS request status. Possible values include: - `PendingKeyHolderConfirmation`: The action done to the TSS request is currently pending enough key share holders to approve.  - `KeyHolderConfirmationFailed`: Key share holders failed to approve the the action to be done to the TSS request.  - `KeyGenerating`: The key share is currently being generated for the action to be done to the TSS request.  - `KeyGeneratingFailed`: The key share generation process has failed for the action to be done to the TSS request.  - `Success`: The action done to the TSS request has been completed successfully. If you see this status while running [Cancel TSS request](/v2/api-references/wallets--mpc-wallets/cancel-tss-request), this mean the specified TSS request has been successfully canceled. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


