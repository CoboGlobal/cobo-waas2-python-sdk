# TSSRequestStatus

The TSS request status. Possible values include: - `PendingKeyHolderConfirmation`: The action done to the TSS request is currently pending enough key share holders to approve.  - `KeyHolderConfirmationFailed`: Key share holders failed to approve the the action to be done to the TSS request.  - `KeyGenerating`: The key share is currently being generated for the action to be done to the TSS request.  - `MPCProcessing`: The TSS request approval is waiting to be started.    - For [MPC Wallets (User-Controlled Wallets)](https://manuals.cobo.com/en/portal/mpc-wallets/ucw/introduction), you need to use the Client App and call the UCW SDK to start the TSS request approval process.   - For [MPC Wallets (Organization-Controlled Wallets)](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/introduction):     - If you are using the [server co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#create-a-main-group), this status indicates that the TSS Node will soon request the callback server to start the [risk controls](https://manuals.cobo.com/en/portal/risk-controls/introduction) check. No further action is required from you at this stage.     - If you are using the [mobile co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#create-a-main-group), key share holders need to use their [Cobo Guard](https://manuals.cobo.com/en/guard/introduction) to approve the TSS request and participate in the signing process.  - `KeyGeneratingFailed`: The key share generation process has failed for the action to be done to the TSS request.  - `Success`: The action done to the TSS request has been completed successfully. If you see this status while running [Cancel TSS request](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/cancel-tss-request), this mean the specified TSS request has been successfully canceled. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


