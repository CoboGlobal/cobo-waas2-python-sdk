# TravelRuleDepositNaturalEntity

Required fields for NATURAL entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_entity_type** | **str** | Specifies the type of entity associated with the transaction. | 
**first_name** | **str** | The first name of the user. | 
**last_name** | **str** | The last name of the user. | 
**date_of_birth** | **date** | The date of birth of the user. This field is required when: - **Calling**: &#x60;travel_rule/transaction/limitation&#x60; API returns &#x60;is_threshold_reached &#x3D; true&#x60;. - **Entity Type**: NATURAL. Otherwise, this field can be omitted.  | [optional] 
**place_of_birth** | **str** | The place of birth of the user. This field is required when: - **Calling**: &#x60;travel_rule/transaction/limitation&#x60; API returns &#x60;is_threshold_reached &#x3D; true&#x60;. - **Entity Type**: NATURAL. Otherwise, this field can be omitted.  | [optional] 

## Example

```python
from cobo_waas2.models.travel_rule_deposit_natural_entity import TravelRuleDepositNaturalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleDepositNaturalEntity from a JSON string
travel_rule_deposit_natural_entity_instance = TravelRuleDepositNaturalEntity.from_json(json)
# print the JSON string representation of the object
print(TravelRuleDepositNaturalEntity.to_json())

# convert the object into a dict
travel_rule_deposit_natural_entity_dict = travel_rule_deposit_natural_entity_instance.to_dict()
# create an instance of TravelRuleDepositNaturalEntity from a dict
travel_rule_deposit_natural_entity_from_dict = TravelRuleDepositNaturalEntity.from_dict(travel_rule_deposit_natural_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


