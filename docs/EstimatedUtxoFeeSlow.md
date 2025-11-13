# EstimatedUtxoFeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | 
**fallback** | **bool** | Indicates whether the estimated fee is generated from Cobo’s fallback mechanism. When the estimated transaction belongs to a UTXO-based chain and the specified address does not have sufficient balance to cover the on-chain fee, this field will be set to &#x60;true&#x60;. In this case, the returned fee value is estimated by Cobo’s internal fallback strategy, which is typically higher than the actual on-chain fee. When &#x60;fallback&#x60; is &#x60;true&#x60;, please use the estimated fee value with caution. | [optional] 
**fee_amount** | **str** | The transaction fee that you need to pay for the transaction. | 

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


