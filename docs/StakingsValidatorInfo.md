# StakingsValidatorInfo

The information about the validator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_url** | **str** | The URL of the validator&#39;s icon. | [optional] 
**public_key** | **str** | The validator&#39;s public key. | [optional] 
**name** | **str** | The validator&#39;s name. | [optional] 
**address** | **str** | The wallet address of the validator. | [optional] 
**commission_rate** | **str** | The commission rate of the validator. | [optional] 

## Example

```python
from cobo_waas2.models.stakings_validator_info import StakingsValidatorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StakingsValidatorInfo from a JSON string
stakings_validator_info_instance = StakingsValidatorInfo.from_json(json)
# print the JSON string representation of the object
print(StakingsValidatorInfo.to_json())

# convert the object into a dict
stakings_validator_info_dict = stakings_validator_info_instance.to_dict()
# create an instance of StakingsValidatorInfo from a dict
stakings_validator_info_from_dict = StakingsValidatorInfo.from_dict(stakings_validator_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


