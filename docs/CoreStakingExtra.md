# CoreStakingExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**pos_chain** | **str** | The Proof-of-Stake (PoS) chain. | 
**staker_address** | **str** | The staker&#39;s Bitcoin address. | 
**validator_address** | **str** | The validator&#39;s EVM address. | 
**reward_address** | **str** | The EVM address to receive staking rewards. | 
**timelock** | **int** | The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal. | 

## Example

```python
from cobo_waas2.models.core_staking_extra import CoreStakingExtra

# TODO update the JSON string below
json = "{}"
# create an instance of CoreStakingExtra from a JSON string
core_staking_extra_instance = CoreStakingExtra.from_json(json)
# print the JSON string representation of the object
print(CoreStakingExtra.to_json())

# convert the object into a dict
core_staking_extra_dict = core_staking_extra_instance.to_dict()
# create an instance of CoreStakingExtra from a dict
core_staking_extra_from_dict = CoreStakingExtra.from_dict(core_staking_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


