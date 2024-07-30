# TransactionTransferToWalletDestination

Information about the transaction destination, which varies depending on whether you are the initiator or the receiver of the transaction.   - As the initiator, you will see detailed information about the transaction destination, and the `destination` will be displayed as one of the following types: `EVM_Contract`, `EVM_EIP_191_Signature`, `EVM_EIP_712_Signature`, `DepositToAddress`, or `DepositToWallet`. `DepositToWallet` indicates the destination is an Exchange Wallet, while `DepositToAddress` indicates the destination is a wallet of other wallet types or an external address. - As the receiver, you will see the `destination` as the type `Address` or `ExchangeWallet`. `Address` indicates the destination is a wallet of other wallet types than Exchange Wallets or an external address. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**sub_wallet_id** | **str** | The exchange trading account or the sub-wallet ID. | [optional] 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | [optional] 
**amount** | **str** | The quantity of the token in the transaction. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.transaction_transfer_to_wallet_destination import TransactionTransferToWalletDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTransferToWalletDestination from a JSON string
transaction_transfer_to_wallet_destination_instance = TransactionTransferToWalletDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionTransferToWalletDestination.to_json())

# convert the object into a dict
transaction_transfer_to_wallet_destination_dict = transaction_transfer_to_wallet_destination_instance.to_dict()
# create an instance of TransactionTransferToWalletDestination from a dict
transaction_transfer_to_wallet_destination_from_dict = TransactionTransferToWalletDestination.from_dict(transaction_transfer_to_wallet_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


