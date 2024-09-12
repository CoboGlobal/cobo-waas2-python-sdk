# AmountStatus

The status of the staking amount. Possible values include:  - `StakeInProgress`: The staking request is submitted and is waiting to be confirmed by the staking protocol. - `Active`: The amount has been staked. - `Rejected`: The staking request has been rejected because the signer refuses to sign the transaction. - `LimitExceeded`: The total staking cap of the staking protocol has been reached. - `Invalid`: The staking request is invalid. This is often due to the failure to broadcast the transaction. - `UnstakeInProgress`: The unstaking request is submitted and is waiting to be confirmed by the staking protocol. - `Withdrawable`: The tokens have been unstaked and are ready to be withdrawn. - `WithdrawInProgress`: The withdrawal request is submitted and is waiting to be confirmed on the chain network. - `Closed`: The staking position is closed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


