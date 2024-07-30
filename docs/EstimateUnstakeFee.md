# EstimateUnstakeFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ActivityType**](ActivityType.md) |  | 
**staking_id** | **str** | The id of the related staking. | 
**amount** | **str** | The amount to stake | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimate_unstake_fee import EstimateUnstakeFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateUnstakeFee from a JSON string
estimate_unstake_fee_instance = EstimateUnstakeFee.from_json(json)
# print the JSON string representation of the object
print(EstimateUnstakeFee.to_json())

# convert the object into a dict
estimate_unstake_fee_dict = estimate_unstake_fee_instance.to_dict()
# create an instance of EstimateUnstakeFee from a dict
estimate_unstake_fee_from_dict = EstimateUnstakeFee.from_dict(estimate_unstake_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


