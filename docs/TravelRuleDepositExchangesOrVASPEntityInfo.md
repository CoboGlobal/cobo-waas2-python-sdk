# TravelRuleDepositExchangesOrVASPEntityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_entity_type** | **str** | Specifies the type of entity associated with the transaction. - &#x60;LEGAL&#x60;: Legal entity. - &#x60;NATURAL&#x60;: Natural person.  | 
**legal_name** | **str** | The legal name of the entity. | 
**date_of_incorporation** | **date** | The date of incorporation of the entity. This field is required when either of the following conditions is met: - &#x60;is_threshold_reached&#x60; is &#x60;true&#x60; in the response of the [Retrieve transaction limitations](https://www.cobo.com/developers/v2/api-references/travelrule/retrieve-transaction-limitations) operation. - &#x60;selected_entity_type&#x60; is &#x60;LEGAL&#x60;.  | [optional] 
**place_of_incorporation** | **str** | The place of incorporation of the entity. This field is required when either of the following conditions is met: - &#x60;is_threshold_reached&#x60; is &#x60;true&#x60; in the response of the [Retrieve transaction limitations](https://www.cobo.com/developers/v2/api-references/travelrule/retrieve-transaction-limitations) operation. - &#x60;selected_entity_type&#x60; is &#x60;LEGAL&#x60;.  | [optional] 
**first_name** | **str** | The first name of the natural person. | 
**last_name** | **str** | The last name of the natural person. | 
**date_of_birth** | **date** | The date of birth of the natural person. This field is required when either of the following conditions is met: - &#x60;is_threshold_reached&#x60; is &#x60;true&#x60; in the response of the [Retrieve transaction limitations](https://www.cobo.com/developers/v2/api-references/travelrule/retrieve-transaction-limitations) operation. - &#x60;selected_entity_type&#x60; is &#x60;NATURAL&#x60;.  | [optional] 
**place_of_birth** | **str** | The place of birth of the natural person. This field is required when either of the following conditions is met: - &#x60;is_threshold_reached&#x60; is &#x60;true&#x60; in the response of the [Retrieve transaction limitations](https://www.cobo.com/developers/v2/api-references/travelrule/retrieve-transaction-limitations) operation. - &#x60;selected_entity_type&#x60; is &#x60;NATURAL&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.travel_rule_deposit_exchanges_or_vasp_entity_info import TravelRuleDepositExchangesOrVASPEntityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleDepositExchangesOrVASPEntityInfo from a JSON string
travel_rule_deposit_exchanges_or_vasp_entity_info_instance = TravelRuleDepositExchangesOrVASPEntityInfo.from_json(json)
# print the JSON string representation of the object
print(TravelRuleDepositExchangesOrVASPEntityInfo.to_json())

# convert the object into a dict
travel_rule_deposit_exchanges_or_vasp_entity_info_dict = travel_rule_deposit_exchanges_or_vasp_entity_info_instance.to_dict()
# create an instance of TravelRuleDepositExchangesOrVASPEntityInfo from a dict
travel_rule_deposit_exchanges_or_vasp_entity_info_from_dict = TravelRuleDepositExchangesOrVASPEntityInfo.from_dict(travel_rule_deposit_exchanges_or_vasp_entity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


