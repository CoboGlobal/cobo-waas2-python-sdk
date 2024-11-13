# EthStakingExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**pos_chain** | **str** | The Proof-of-Stake (PoS) chain. | 

## Example

```python
from cobo_waas2.models.eth_staking_extra import EthStakingExtra

# TODO update the JSON string below
json = "{}"
# create an instance of EthStakingExtra from a JSON string
eth_staking_extra_instance = EthStakingExtra.from_json(json)
# print the JSON string representation of the object
print(EthStakingExtra.to_json())

# convert the object into a dict
eth_staking_extra_dict = eth_staking_extra_instance.to_dict()
# create an instance of EthStakingExtra from a dict
eth_staking_extra_from_dict = EthStakingExtra.from_dict(eth_staking_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


