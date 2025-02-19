# EthStakingActivityDetailExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**provider_name** | **str** | The name of the provider. | [optional] 
**validator_pubkeys** | **List[str]** | A list of public keys associated with the Ethereum validators for this unstaking operation. | [optional] 

## Example

```python
from cobo_waas2.models.eth_staking_activity_detail_extra import EthStakingActivityDetailExtra

# TODO update the JSON string below
json = "{}"
# create an instance of EthStakingActivityDetailExtra from a JSON string
eth_staking_activity_detail_extra_instance = EthStakingActivityDetailExtra.from_json(json)
# print the JSON string representation of the object
print(EthStakingActivityDetailExtra.to_json())

# convert the object into a dict
eth_staking_activity_detail_extra_dict = eth_staking_activity_detail_extra_instance.to_dict()
# create an instance of EthStakingActivityDetailExtra from a dict
eth_staking_activity_detail_extra_from_dict = EthStakingActivityDetailExtra.from_dict(eth_staking_activity_detail_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


