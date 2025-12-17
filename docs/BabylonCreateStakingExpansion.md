# BabylonCreateStakingExpansion

The staking expansion information specific to the Babylon protocol.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_id** | **str** | The ID of the Phase-2 BTC staking position. | 
**finality_provider_public_keys** | **List[str]** | The public keys of the finality providers, with each key corresponding to a BSN chain. | 
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 

## Example

```python
from cobo_waas2.models.babylon_create_staking_expansion import BabylonCreateStakingExpansion

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonCreateStakingExpansion from a JSON string
babylon_create_staking_expansion_instance = BabylonCreateStakingExpansion.from_json(json)
# print the JSON string representation of the object
print(BabylonCreateStakingExpansion.to_json())

# convert the object into a dict
babylon_create_staking_expansion_dict = babylon_create_staking_expansion_instance.to_dict()
# create an instance of BabylonCreateStakingExpansion from a dict
babylon_create_staking_expansion_from_dict = BabylonCreateStakingExpansion.from_dict(babylon_create_staking_expansion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


