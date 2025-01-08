# TravelRuleDepositLegalEntity

Required fields for LEGAL entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_entity_type** | **str** | Specifies the type of entity associated with the transaction. | 
**legal_name** | **str** | The legal name of the entity. | 
**date_of_incorporation** | **date** | The incorporation date of the entity. This field is required when: - **Calling**: &#x60;travel_rule/transaction/limitation&#x60; API returns &#x60;is_threshold_reached &#x3D; true&#x60;. - **Entity Type**: LEGAL. Otherwise, this field can be omitted.  | [optional] 
**place_of_incorporation** | **str** | The place of incorporation of the entity. This field is required when: - **Calling**: &#x60;travel_rule/transaction/limitation&#x60; API returns &#x60;is_threshold_reached &#x3D; true&#x60;. - **Entity Type**: LEGAL. Otherwise, this field can be omitted.  | [optional] 

## Example

```python
from cobo_waas2.models.travel_rule_deposit_legal_entity import TravelRuleDepositLegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleDepositLegalEntity from a JSON string
travel_rule_deposit_legal_entity_instance = TravelRuleDepositLegalEntity.from_json(json)
# print the JSON string representation of the object
print(TravelRuleDepositLegalEntity.to_json())

# convert the object into a dict
travel_rule_deposit_legal_entity_dict = travel_rule_deposit_legal_entity_instance.to_dict()
# create an instance of TravelRuleDepositLegalEntity from a dict
travel_rule_deposit_legal_entity_from_dict = TravelRuleDepositLegalEntity.from_dict(travel_rule_deposit_legal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


