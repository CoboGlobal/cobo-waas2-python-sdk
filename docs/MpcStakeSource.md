# MpcStakeSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**StakeSourceType**](StakeSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 

## Example

```python
from cobo_waas2.models.mpc_stake_source import MpcStakeSource

# TODO update the JSON string below
json = "{}"
# create an instance of MpcStakeSource from a JSON string
mpc_stake_source_instance = MpcStakeSource.from_json(json)
# print the JSON string representation of the object
print(MpcStakeSource.to_json())

# convert the object into a dict
mpc_stake_source_dict = mpc_stake_source_instance.to_dict()
# create an instance of MpcStakeSource from a dict
mpc_stake_source_from_dict = MpcStakeSource.from_dict(mpc_stake_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


