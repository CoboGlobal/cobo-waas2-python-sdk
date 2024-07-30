# BaseStakeExtra

Base stake extra.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 

## Example

```python
from cobo_waas2.models.base_stake_extra import BaseStakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStakeExtra from a JSON string
base_stake_extra_instance = BaseStakeExtra.from_json(json)
# print the JSON string representation of the object
print(BaseStakeExtra.to_json())

# convert the object into a dict
base_stake_extra_dict = base_stake_extra_instance.to_dict()
# create an instance of BaseStakeExtra from a dict
base_stake_extra_from_dict = BaseStakeExtra.from_dict(base_stake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


