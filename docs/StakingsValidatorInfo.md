# StakingsValidatorInfo

The validator info of the stake.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_url** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**commission_rate** | **str** |  | [optional] 

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


