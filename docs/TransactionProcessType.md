# TransactionProcessType

Transaction processing type. This property applies to MPC Wallets and Custodial Wallets (Web3 Wallets) only. Possible values are: - `AutoProcess` (default): After the transaction is constructed, it will be automatically signed and broadcast. - `BuildOnly`: Set to this value if you want to build the transaction first without automatically signing and broadcasting it. You can manually call the [Sign and broadcast transaction](https://www.cobo.com/developers/v2/api-references/transactions/sign-and-broadcast-transaction) operation to complete the signing and broadcasting process. - `SignOnly`: Set to this value if you want to build and sign the transaction first without automatically broadcasting it. You can manually call the [Broadcast signed transactions](https://www.cobo.com/developers/v2/api-references/transactions/broadcast-signed-transactions) operation to broadcast the transaction to the blockchain. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


