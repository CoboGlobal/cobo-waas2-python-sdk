# TransactionSelectedUtxo

The selected UTXO information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** | The transaction hash of the UTXO. | [optional] 
**vout_n** | **int** | The output index of the UTXO. | [optional] 
**address** | **str** | The address of the UTXO. | [optional] 
**value** | **str** | The value of the UTXO. | [optional] 
**redeem_script** | **str** | The redeem script used in P2SH and P2WSH transactions. | [optional] 
**revealed_script** | **str** | The revealed script used for Taproot script-path spend transaction. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_selected_utxo import TransactionSelectedUtxo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSelectedUtxo from a JSON string
transaction_selected_utxo_instance = TransactionSelectedUtxo.from_json(json)
# print the JSON string representation of the object
print(TransactionSelectedUtxo.to_json())

# convert the object into a dict
transaction_selected_utxo_dict = transaction_selected_utxo_instance.to_dict()
# create an instance of TransactionSelectedUtxo from a dict
transaction_selected_utxo_from_dict = TransactionSelectedUtxo.from_dict(transaction_selected_utxo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


