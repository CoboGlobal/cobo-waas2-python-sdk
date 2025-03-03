# TransactionRawTxInfo

The raw transaction information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_nonce** | **int** | The transaction nonce. | [optional] 
**selected_utxos** | [**List[TransactionSelectedUtxo]**](TransactionSelectedUtxo.md) | The selected UTXOs to be consumed in the transaction. | [optional] 
**raw_tx** | **str** | The raw transaction data. | [optional] 
**unsigned_raw_tx** | **str** | The unsigned raw transaction data. | [optional] 
**utxo_change** | [**TransactionUtxoChange**](TransactionUtxoChange.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_raw_tx_info import TransactionRawTxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRawTxInfo from a JSON string
transaction_raw_tx_info_instance = TransactionRawTxInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionRawTxInfo.to_json())

# convert the object into a dict
transaction_raw_tx_info_dict = transaction_raw_tx_info_instance.to_dict()
# create an instance of TransactionRawTxInfo from a dict
transaction_raw_tx_info_from_dict = TransactionRawTxInfo.from_dict(transaction_raw_tx_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


