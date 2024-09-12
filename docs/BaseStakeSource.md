# BaseStakeSource

The information about the staking source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**StakeSourceType**](StakeSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 

## Example

```python
from cobo_waas2.models.base_stake_source import BaseStakeSource

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStakeSource from a JSON string
base_stake_source_instance = BaseStakeSource.from_json(json)
# print the JSON string representation of the object
print(BaseStakeSource.to_json())

# convert the object into a dict
base_stake_source_dict = base_stake_source_instance.to_dict()
# create an instance of BaseStakeSource from a dict
base_stake_source_from_dict = BaseStakeSource.from_dict(base_stake_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


