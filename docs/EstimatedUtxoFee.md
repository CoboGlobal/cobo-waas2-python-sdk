# EstimatedUtxoFee

The estimated transaction fee for UTXO-based chains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**slow** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | 
**fast** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimated_utxo_fee import EstimatedUtxoFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedUtxoFee from a JSON string
estimated_utxo_fee_instance = EstimatedUtxoFee.from_json(json)
# print the JSON string representation of the object
print(EstimatedUtxoFee.to_json())

# convert the object into a dict
estimated_utxo_fee_dict = estimated_utxo_fee_instance.to_dict()
# create an instance of EstimatedUtxoFee from a dict
estimated_utxo_fee_from_dict = EstimatedUtxoFee.from_dict(estimated_utxo_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


