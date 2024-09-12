# BabylonStakingExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**pos_chain** | **str** | The Proof-of-Stake (PoS) chain. | 
**unlock_timestamp** | **int** | The estimated time when the bitcoins will be unlocked, in Unix timestamp format, measured in milliseconds. | [optional] 
**unlock_block_height** | **int** | The block height at which the bitcoins will be unlocked. | [optional] 
**stake_address** | **str** | The address receiving the staked bitcoins. | [optional] 
**unbond_address** | **str** | The address receiving the unlocked bitcoins. | [optional] 

## Example

```python
from cobo_waas2.models.babylon_staking_extra import BabylonStakingExtra

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonStakingExtra from a JSON string
babylon_staking_extra_instance = BabylonStakingExtra.from_json(json)
# print the JSON string representation of the object
print(BabylonStakingExtra.to_json())

# convert the object into a dict
babylon_staking_extra_dict = babylon_staking_extra_instance.to_dict()
# create an instance of BabylonStakingExtra from a dict
babylon_staking_extra_from_dict = BabylonStakingExtra.from_dict(babylon_staking_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


