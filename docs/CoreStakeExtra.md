# CoreStakeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**timelock** | **int** | The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal. | 
**change_address** | **str** | The change address on the Bitcoin chain. If not provided, the source wallet&#39;s address will be used as the change address. | [optional] 
**validator_address** | **str** | The validator&#39;s EVM address. | 
**reward_address** | **str** | The EVM address to receive staking rewards. | 

## Example

```python
from cobo_waas2.models.core_stake_extra import CoreStakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of CoreStakeExtra from a JSON string
core_stake_extra_instance = CoreStakeExtra.from_json(json)
# print the JSON string representation of the object
print(CoreStakeExtra.to_json())

# convert the object into a dict
core_stake_extra_dict = core_stake_extra_instance.to_dict()
# create an instance of CoreStakeExtra from a dict
core_stake_extra_from_dict = CoreStakeExtra.from_dict(core_stake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


