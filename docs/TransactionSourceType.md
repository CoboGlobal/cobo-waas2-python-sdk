# TransactionSourceType

The transaction source. Possible values include:   - `Asset`: A Custodial Wallet (Asset Wallet).   - `Org-Controlled`: An MPC Wallet (Organization-Controlled Wallet).   - `User-Controlled`: An MPC Wallet (User-Controlled Wallet).   - `Safe{Wallet}`: A Smart Contract Wallet (Safe{Wallet}).   - `Main`: An Exchange Wallet (Main Account).   - `Sub`: An Exchange Wallet (Sub Account).   - `DepositFromAddress`: An address that can be a Cobo's wallet address or an external address.   - `DepositFromWallet`: An Exchange Wallet.   - `DepositFromLoop`: A transfer sender through the Loop transfer network.  For the same transaction, the transaction source varies depending on whether you are the initiator or the receiver of the transaction.     - As the initiator, you will see detailed information about the transaction source, and the `source` will be displayed as one of the following wallet sub-types: `Asset`, `Org-Controlled`, `User-Controlled`, `Safe{Wallet}`, `Main`, or `Sub`.   - As the receiver, you will see the `source` as either `DepositFromAddress`, `DepositFromWallet`, or `DepositFromLoop`. If the transaction is from the Loop transfer network, the source will be `DepositFromLoop`. Otherwise, it will be either `DepositFromWallet` (indicating an Exchange Wallet) or `DepositFromAddress` (indicating other wallet type than an Exchange Wallet or an external address). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


