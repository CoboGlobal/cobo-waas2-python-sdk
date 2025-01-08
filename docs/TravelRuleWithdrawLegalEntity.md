# TravelRuleWithdrawLegalEntity

Required fields for LEGAL entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_entity_type** | [**SelectedEntityType**](SelectedEntityType.md) |  | 
**legal_name** | **str** | The legal name of the entity. | 
**date_of_incorporation** | **date** | The incorporation date of the entity. | [optional] 
**place_of_incorporation** | **str** | The place of incorporation of the entity. | [optional] 

## Example

```python
from cobo_waas2.models.travel_rule_withdraw_legal_entity import TravelRuleWithdrawLegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleWithdrawLegalEntity from a JSON string
travel_rule_withdraw_legal_entity_instance = TravelRuleWithdrawLegalEntity.from_json(json)
# print the JSON string representation of the object
print(TravelRuleWithdrawLegalEntity.to_json())

# convert the object into a dict
travel_rule_withdraw_legal_entity_dict = travel_rule_withdraw_legal_entity_instance.to_dict()
# create an instance of TravelRuleWithdrawLegalEntity from a dict
travel_rule_withdraw_legal_entity_from_dict = TravelRuleWithdrawLegalEntity.from_dict(travel_rule_withdraw_legal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


