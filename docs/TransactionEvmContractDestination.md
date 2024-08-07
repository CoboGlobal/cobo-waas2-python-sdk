# TransactionEvmContractDestination

Information about the transaction destination type `EVM_Contract`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**address** | **str** | The destination address. | 
**value** | **str** | The quantity of the token in the transaction. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 
**calldata** | **bytearray** | The data that is used to invoke a specific function or method within the specified contract at the destination address.  | 

## Example

```python
from cobo_waas2.models.transaction_evm_contract_destination import TransactionEvmContractDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEvmContractDestination from a JSON string
transaction_evm_contract_destination_instance = TransactionEvmContractDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionEvmContractDestination.to_json())

# convert the object into a dict
transaction_evm_contract_destination_dict = transaction_evm_contract_destination_instance.to_dict()
# create an instance of TransactionEvmContractDestination from a dict
transaction_evm_contract_destination_from_dict = TransactionEvmContractDestination.from_dict(transaction_evm_contract_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


