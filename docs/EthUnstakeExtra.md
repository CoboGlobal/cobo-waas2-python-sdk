# EthUnstakeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**validator_pubkeys** | **List[str]** | A list of public keys identifying the validators to unstake from the Ethereum Beacon Chain. | 

## Example

```python
from cobo_waas2.models.eth_unstake_extra import EthUnstakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of EthUnstakeExtra from a JSON string
eth_unstake_extra_instance = EthUnstakeExtra.from_json(json)
# print the JSON string representation of the object
print(EthUnstakeExtra.to_json())

# convert the object into a dict
eth_unstake_extra_dict = eth_unstake_extra_instance.to_dict()
# create an instance of EthUnstakeExtra from a dict
eth_unstake_extra_from_dict = EthUnstakeExtra.from_dict(eth_unstake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


