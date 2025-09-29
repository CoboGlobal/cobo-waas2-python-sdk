# UtxoFeeBasePrice

The transaction fee rate for UTXO-based chains (such as Bitcoin).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | [optional] 

## Example

```python
from cobo_waas2.models.utxo_fee_base_price import UtxoFeeBasePrice

# TODO update the JSON string below
json = "{}"
# create an instance of UtxoFeeBasePrice from a JSON string
utxo_fee_base_price_instance = UtxoFeeBasePrice.from_json(json)
# print the JSON string representation of the object
print(UtxoFeeBasePrice.to_json())

# convert the object into a dict
utxo_fee_base_price_dict = utxo_fee_base_price_instance.to_dict()
# create an instance of UtxoFeeBasePrice from a dict
utxo_fee_base_price_from_dict = UtxoFeeBasePrice.from_dict(utxo_fee_base_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


