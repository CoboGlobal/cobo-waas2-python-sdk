# UTXO

The UTXO information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** | The transaction hash of the UTXO. | [optional] 
**vout_n** | **int** | The output index of the UTXO. | [optional] 
**address** | **str** | The address of the UTXO. | [optional] 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | [optional] 
**value** | **str** | The value of the UTXO. | [optional] 
**is_coinbase** | **bool** | Whether the UTXO comes from a coinbase transaction. | [optional] 
**is_locked** | **bool** | Whether the UTXO is locked. | [optional] 
**confirmed_number** | **int** | The number of confirmations for the UTXO. | [optional] 
**is_frozen** | **bool** | Whether the UTXO is frozen. | [optional] 

## Example

```python
from cobo_waas2.models.utxo import UTXO

# TODO update the JSON string below
json = "{}"
# create an instance of UTXO from a JSON string
utxo_instance = UTXO.from_json(json)
# print the JSON string representation of the object
print(UTXO.to_json())

# convert the object into a dict
utxo_dict = utxo_instance.to_dict()
# create an instance of UTXO from a dict
utxo_from_dict = UTXO.from_dict(utxo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


