# CoreStakingActivityDetailExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**timelock** | **int** | The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal. | [optional] 
**change_address** | **str** | The change address on the Bitcoin chain. If not provided, the source wallet&#39;s address will be used as the change address. | [optional] 
**validator_address** | **str** | The validator&#39;s EVM address. | [optional] 
**reward_address** | **str** | The EVM address to receive staking rewards. | [optional] 

## Example

```python
from cobo_waas2.models.core_staking_activity_detail_extra import CoreStakingActivityDetailExtra

# TODO update the JSON string below
json = "{}"
# create an instance of CoreStakingActivityDetailExtra from a JSON string
core_staking_activity_detail_extra_instance = CoreStakingActivityDetailExtra.from_json(json)
# print the JSON string representation of the object
print(CoreStakingActivityDetailExtra.to_json())

# convert the object into a dict
core_staking_activity_detail_extra_dict = core_staking_activity_detail_extra_instance.to_dict()
# create an instance of CoreStakingActivityDetailExtra from a dict
core_staking_activity_detail_extra_from_dict = CoreStakingActivityDetailExtra.from_dict(core_staking_activity_detail_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


