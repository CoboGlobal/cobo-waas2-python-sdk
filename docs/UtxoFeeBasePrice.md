# UtxoFeeBasePrice

The transaction fee rate for UTXO-based chains (such as Bitcoin).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | [optional] 
**fallback** | **bool** | Indicates whether the estimated fee is generated from Cobo’s fallback mechanism. When the estimated transaction belongs to a UTXO-based chain and the specified address does not have sufficient balance to cover the on-chain fee, this field will be set to &#x60;true&#x60;. In this case, the returned fee value is estimated by Cobo’s internal fallback strategy, which is typically higher than the actual on-chain fee. When &#x60;fallback&#x60; is &#x60;true&#x60;, please use the estimated fee value with caution. | [optional] 

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


