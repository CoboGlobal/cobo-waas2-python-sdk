# TransactionTransferToAddressDestinationUtxoOutputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The destination address. | [optional] 
**amount** | **str** | The quantity of the token in the transaction. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 
**script** | **str** | The script of the output. It is a programmable code fragment that defines the conditions under which the UTXO can be spent. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_transfer_to_address_destination_utxo_outputs_inner import TransactionTransferToAddressDestinationUtxoOutputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTransferToAddressDestinationUtxoOutputsInner from a JSON string
transaction_transfer_to_address_destination_utxo_outputs_inner_instance = TransactionTransferToAddressDestinationUtxoOutputsInner.from_json(json)
# print the JSON string representation of the object
print(TransactionTransferToAddressDestinationUtxoOutputsInner.to_json())

# convert the object into a dict
transaction_transfer_to_address_destination_utxo_outputs_inner_dict = transaction_transfer_to_address_destination_utxo_outputs_inner_instance.to_dict()
# create an instance of TransactionTransferToAddressDestinationUtxoOutputsInner from a dict
transaction_transfer_to_address_destination_utxo_outputs_inner_from_dict = TransactionTransferToAddressDestinationUtxoOutputsInner.from_dict(transaction_transfer_to_address_destination_utxo_outputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


