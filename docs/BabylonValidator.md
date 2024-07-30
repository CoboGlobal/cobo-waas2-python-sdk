# BabylonValidator

The babylon validator information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_url** | **str** | The URL of the validator&#39;s icon. | 
**name** | **str** | The name of validator. | 
**priority** | **int** | The priority of validator. | [optional] 
**public_key** | **str** | The public key of validator. | 
**commission_rate** | **float** | The commission rate of validator. | 
**supported_pos_chains** | **List[str]** | The list of supported pos chains. | 

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


