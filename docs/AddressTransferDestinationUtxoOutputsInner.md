# AddressTransferDestinationUtxoOutputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The destination address. | 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | [optional] 
**script** | **str** | The script of the output. It is a programmable code fragment that defines the conditions under which the UTXO can be spent. | [optional] 

## Example

```python
from cobo_waas2.models.address_transfer_destination_utxo_outputs_inner import AddressTransferDestinationUtxoOutputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTransferDestinationUtxoOutputsInner from a JSON string
address_transfer_destination_utxo_outputs_inner_instance = AddressTransferDestinationUtxoOutputsInner.from_json(json)
# print the JSON string representation of the object
print(AddressTransferDestinationUtxoOutputsInner.to_json())

# convert the object into a dict
address_transfer_destination_utxo_outputs_inner_dict = address_transfer_destination_utxo_outputs_inner_instance.to_dict()
# create an instance of AddressTransferDestinationUtxoOutputsInner from a dict
address_transfer_destination_utxo_outputs_inner_from_dict = AddressTransferDestinationUtxoOutputsInner.from_dict(address_transfer_destination_utxo_outputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


