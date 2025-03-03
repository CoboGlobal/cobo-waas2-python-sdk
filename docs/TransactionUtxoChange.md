# TransactionUtxoChange

The UTXO change output information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The receiving address of the UTXO change output. | [optional] 
**value** | **str** | The amount of the UTXO change output. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_utxo_change import TransactionUtxoChange

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUtxoChange from a JSON string
transaction_utxo_change_instance = TransactionUtxoChange.from_json(json)
# print the JSON string representation of the object
print(TransactionUtxoChange.to_json())

# convert the object into a dict
transaction_utxo_change_dict = transaction_utxo_change_instance.to_dict()
# create an instance of TransactionUtxoChange from a dict
transaction_utxo_change_from_dict = TransactionUtxoChange.from_dict(transaction_utxo_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


