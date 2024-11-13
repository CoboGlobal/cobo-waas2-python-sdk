# BabylonStakeEstimatedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | [optional] 
**fee_amount** | **str** | The amount of the estimated fee. | [optional] 
**token_id** | **str** | The token ID of the staking fee. | [optional] 

## Example

```python
from cobo_waas2.models.babylon_stake_estimated_fee import BabylonStakeEstimatedFee

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonStakeEstimatedFee from a JSON string
babylon_stake_estimated_fee_instance = BabylonStakeEstimatedFee.from_json(json)
# print the JSON string representation of the object
print(BabylonStakeEstimatedFee.to_json())

# convert the object into a dict
babylon_stake_estimated_fee_dict = babylon_stake_estimated_fee_instance.to_dict()
# create an instance of BabylonStakeEstimatedFee from a dict
babylon_stake_estimated_fee_from_dict = BabylonStakeEstimatedFee.from_dict(babylon_stake_estimated_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


