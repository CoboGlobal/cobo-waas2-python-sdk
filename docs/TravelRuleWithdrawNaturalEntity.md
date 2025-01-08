# TravelRuleWithdrawNaturalEntity

Required fields for NATURAL entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_entity_type** | [**SelectedEntityType**](SelectedEntityType.md) |  | 
**first_name** | **str** | The first name of the user. | 
**last_name** | **str** | The last name of the user. | 
**date_of_birth** | **date** | The date of birth of the user. | [optional] 
**place_of_birth** | **str** | The place of birth of the user. | [optional] 

## Example

```python
from cobo_waas2.models.travel_rule_withdraw_natural_entity import TravelRuleWithdrawNaturalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleWithdrawNaturalEntity from a JSON string
travel_rule_withdraw_natural_entity_instance = TravelRuleWithdrawNaturalEntity.from_json(json)
# print the JSON string representation of the object
print(TravelRuleWithdrawNaturalEntity.to_json())

# convert the object into a dict
travel_rule_withdraw_natural_entity_dict = travel_rule_withdraw_natural_entity_instance.to_dict()
# create an instance of TravelRuleWithdrawNaturalEntity from a dict
travel_rule_withdraw_natural_entity_from_dict = TravelRuleWithdrawNaturalEntity.from_dict(travel_rule_withdraw_natural_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


