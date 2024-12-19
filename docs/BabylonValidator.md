# BabylonValidator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**icon_url** | **str** | The URL of the validator&#39;s icon. | [optional] 
**name** | **str** | The validator&#39;s name. | 
**priority** | **int** | This property can be ignored. | [optional] 
**public_key** | **str** | The public key of the validator. | [optional] 
**commission_rate** | **float** | The commission rate of the validator. | [optional] 
**supported_pos_chains** | **List[str]** | A list of supported Proof-of-Stake (PoS) chains. | [optional] 

## Example

```python
from cobo_waas2.models.babylon_validator import BabylonValidator

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonValidator from a JSON string
babylon_validator_instance = BabylonValidator.from_json(json)
# print the JSON string representation of the object
print(BabylonValidator.to_json())

# convert the object into a dict
babylon_validator_dict = babylon_validator_instance.to_dict()
# create an instance of BabylonValidator from a dict
babylon_validator_from_dict = BabylonValidator.from_dict(babylon_validator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


