# TransactionMessageSignEIP191Destination

Information about the transaction destination, which varies depending on whether you are the initiator or the receiver of the transaction.   - As the initiator, you will see detailed information about the transaction destination, and the `destination` will be displayed as one of the following types: `EVM_Contract`, `EVM_EIP_191_Signature`, `EVM_EIP_712_Signature`, `DepositToAddress`, or `DepositToWallet`. `DepositToWallet` indicates the destination is an Exchange Wallet, while `DepositToAddress` indicates the destination is a wallet of other wallet types or an external address. - As the receiver, you will see the `destination` as the type `Address` or `ExchangeWallet`. `Address` indicates the destination is a wallet of other wallet types than Exchange Wallets or an external address. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**message** | **str** | The raw data of the message to be signed, encoded in Base64 format. | 

## Example

```python
from cobo_waas2.models.transaction_message_sign_eip191_destination import TransactionMessageSignEIP191Destination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageSignEIP191Destination from a JSON string
transaction_message_sign_eip191_destination_instance = TransactionMessageSignEIP191Destination.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageSignEIP191Destination.to_json())

# convert the object into a dict
transaction_message_sign_eip191_destination_dict = transaction_message_sign_eip191_destination_instance.to_dict()
# create an instance of TransactionMessageSignEIP191Destination from a dict
transaction_message_sign_eip191_destination_from_dict = TransactionMessageSignEIP191Destination.from_dict(transaction_message_sign_eip191_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


