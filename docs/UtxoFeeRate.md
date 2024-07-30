# UtxoFeeRate

The transaction fee rate for UTXO-based chains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**slow** | [**UtxoFeeBasePrice**](UtxoFeeBasePrice.md) |  | [optional] 
**recommended** | [**UtxoFeeBasePrice**](UtxoFeeBasePrice.md) |  | 
**fast** | [**UtxoFeeBasePrice**](UtxoFeeBasePrice.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.utxo_fee_rate import UtxoFeeRate

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoFeeRate from a JSON string
utxo_fee_rate_instance = UtxoFeeRate.from_json(json)
# print the JSON string representation of the object
print(UtxoFeeRate.to_json())

# convert the object into a dict
utxo_fee_rate_dict = utxo_fee_rate_instance.to_dict()
# create an instance of UtxoFeeRate from a dict
utxo_fee_rate_from_dict = UtxoFeeRate.from_dict(utxo_fee_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


