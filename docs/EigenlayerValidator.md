# EigenlayerValidator

The EigenLayer validator info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_url** | **str** | The URL of the validator&#39;s icon. | 
**name** | **str** | The name of validator. | 
**priority** | **int** | The priority of validator. | [optional] 
**address** | **str** | The address of validator. | 
**commission_rate** | **float** | The commission of validator. | [optional] 

## Example

```python
from cobo_waas2.models.eigenlayer_validator import EigenlayerValidator

# TODO update the JSON string below
json = "{}"
# create an instance of EigenlayerValidator from a JSON string
eigenlayer_validator_instance = EigenlayerValidator.from_json(json)
# print the JSON string representation of the object
print(EigenlayerValidator.to_json())

# convert the object into a dict
eigenlayer_validator_dict = eigenlayer_validator_instance.to_dict()
# create an instance of EigenlayerValidator from a dict
eigenlayer_validator_from_dict = EigenlayerValidator.from_dict(eigenlayer_validator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


