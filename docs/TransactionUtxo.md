# TransactionUtxo

The UTXO information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** | The transaction hash of the UTXO. | [optional] 
**vout_n** | **int** | The output index of the UTXO. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_utxo import TransactionUtxo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUtxo from a JSON string
transaction_utxo_instance = TransactionUtxo.from_json(json)
# print the JSON string representation of the object
print(TransactionUtxo.to_json())

# convert the object into a dict
transaction_utxo_dict = transaction_utxo_instance.to_dict()
# create an instance of TransactionUtxo from a dict
transaction_utxo_from_dict = TransactionUtxo.from_dict(transaction_utxo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


