# TravelRuleDepositLegalEntity

The required information of a legal entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_entity_type** | **str** | The entity type. Possible values include: - &#x60;LEGAL&#x60;: Legal entity. - &#x60;NATURAL&#x60;: Natural person.  | 
**legal_name** | **str** | The legal name of the entity. | 
**date_of_incorporation** | **date** | The date of incorporation of the entity. This field is required when either of the following conditions is met: - &#x60;is_threshold_reached&#x60; is &#x60;true&#x60; in the response of the [Retrieve transaction limitations](https://www.cobo.com/developers/v2/api-references/travelrule/retrieve-transaction-limitations) operation. - &#x60;selected_entity_type&#x60; is &#x60;LEGAL&#x60;.  | [optional] 
**place_of_incorporation** | **str** | The place of incorporation of the entity. This field is required when either of the following conditions is met: - &#x60;is_threshold_reached&#x60; is &#x60;true&#x60; in the response of the [Retrieve transaction limitations](https://www.cobo.com/developers/v2/api-references/travelrule/retrieve-transaction-limitations) operation. - &#x60;selected_entity_type&#x60; is &#x60;LEGAL&#x60;.  | [optional] 

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


