# CreateStakeActivityExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**finality_provider_public_key** | **str** | The public key of finality provider. | 
**stake_block_time** | **int** | The stake block time. | 
**operator** | **str** | The operator address. | [optional] 
**fee_recipient** | **float** | The fee recipient address, if not provided the staker address will be used. | [optional] 

## Example

```python
from cobo_waas2.models.create_stake_activity_extra import CreateStakeActivityExtra

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStakeActivityExtra from a JSON string
create_stake_activity_extra_instance = CreateStakeActivityExtra.from_json(json)
# print the JSON string representation of the object
print(CreateStakeActivityExtra.to_json())

# convert the object into a dict
create_stake_activity_extra_dict = create_stake_activity_extra_instance.to_dict()
# create an instance of CreateStakeActivityExtra from a dict
create_stake_activity_extra_from_dict = CreateStakeActivityExtra.from_dict(create_stake_activity_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


