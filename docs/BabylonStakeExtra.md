# BabylonStakeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**finality_provider_public_key** | **str** | The public key of finality provider. | 
**stake_block_time** | **int** | The stake block time. | 
**only_sign** | **bool** | Whether to only sign transactions. Default is &#x60;false&#x60;, if set to &#x60;true&#x60;,  the transaction will not be submitted to the blockchain automatically. You can call &#x60;Broadcast transactions&#x60; to submit the transaction to the blockchain,  Or you can find the signed raw_tx by &#x60;Get transaction information&#x60; and broadcast it yourself.  | [optional] 

## Example

```python
from cobo_waas2.models.babylon_stake_extra import BabylonStakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonStakeExtra from a JSON string
babylon_stake_extra_instance = BabylonStakeExtra.from_json(json)
# print the JSON string representation of the object
print(BabylonStakeExtra.to_json())

# convert the object into a dict
babylon_stake_extra_dict = babylon_stake_extra_instance.to_dict()
# create an instance of BabylonStakeExtra from a dict
babylon_stake_extra_from_dict = BabylonStakeExtra.from_dict(babylon_stake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


