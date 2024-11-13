# EthStakeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**provider_name** | **str** | The name of the provider. | 

## Example

```python
from cobo_waas2.models.eth_stake_extra import EthStakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of EthStakeExtra from a JSON string
eth_stake_extra_instance = EthStakeExtra.from_json(json)
# print the JSON string representation of the object
print(EthStakeExtra.to_json())

# convert the object into a dict
eth_stake_extra_dict = eth_stake_extra_instance.to_dict()
# create an instance of EthStakeExtra from a dict
eth_stake_extra_from_dict = EthStakeExtra.from_dict(eth_stake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


