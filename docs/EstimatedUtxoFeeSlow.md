# EstimatedUtxoFeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | 
**fee_amount** | **str** | The fee that you need to pay for the transaction. | 

## Example

```python
from cobo_waas2.models.estimated_utxo_fee_slow import EstimatedUtxoFeeSlow

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedUtxoFeeSlow from a JSON string
estimated_utxo_fee_slow_instance = EstimatedUtxoFeeSlow.from_json(json)
# print the JSON string representation of the object
print(EstimatedUtxoFeeSlow.to_json())

# convert the object into a dict
estimated_utxo_fee_slow_dict = estimated_utxo_fee_slow_instance.to_dict()
# create an instance of EstimatedUtxoFeeSlow from a dict
estimated_utxo_fee_slow_from_dict = EstimatedUtxoFeeSlow.from_dict(estimated_utxo_fee_slow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


