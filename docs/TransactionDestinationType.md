# TransactionDestinationType

The transaction destination type. Possible values include:   - `Address`: An address transfer destination, including an address of Custodial Wallets, MPC Wallets, or Smart Contract Wallets (Safe{Wallet}) and an external address.   - `ExchangeWallet`: An Exchange Wallet transfer destination.   - `EVM_Contract`: An EVM compatible contract.   - `EVM_EIP_191_Signature`: An EVM EIP-191 signature. For more details, see [Signed Data Standard](https://eips.ethereum.org/EIPS/eip-191).   - `EVM_EIP_712_Signature`: An EVM EIP-712 signature. For more details, see [Typed structured data hashing and signing](https://eips.ethereum.org/EIPS/eip-712).   - `DepositToAddress`: An address that can be a Cobo's wallet address or an external address.   - `DepositToWallet`: An Exchange Wallet.  For the same transaction, the transaction destination varies depending on whether you are the initiator or the receiver of the transaction.     - As the initiator, you will see detailed information about the transaction destination, and the `destination` will be displayed as one of the following types: `EVM_Contract`, `EVM_EIP_191_Signature`, `EVM_EIP_712_Signature`, `DepositToAddress`, or `DepositToWallet`. `DepositToWallet` indicates the destination is an Exchange Wallet, while `DepositToAddress` indicates the destination is a wallet of other wallet types or an external address.   - As the receiver, you will see the `destination` as the type `Address` or `ExchangeWallet`. `Address` indicates the destination is a wallet of other wallet types than Exchange Wallets or an external address. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


