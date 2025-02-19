# TravelRuleWithdrawExchangesOrVASPEntityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_entity_type** | [**SelectedEntityType**](SelectedEntityType.md) |  | 
**legal_name** | **str** | The legal name of the entity. | 
**date_of_incorporation** | **date** | The date of incorporation of the entity. | [optional] 
**place_of_incorporation** | **str** | The place of incorporation of the entity. | [optional] 
**first_name** | **str** | The first name of the natural person. | 
**last_name** | **str** | The last name of the natural person. | 
**date_of_birth** | **date** | The date of birth of the natural person. | [optional] 
**place_of_birth** | **str** | The place of birth of the natural person. | [optional] 

## Example

```python
from cobo_waas2.models.travel_rule_withdraw_exchanges_or_vasp_entity_info import TravelRuleWithdrawExchangesOrVASPEntityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleWithdrawExchangesOrVASPEntityInfo from a JSON string
travel_rule_withdraw_exchanges_or_vasp_entity_info_instance = TravelRuleWithdrawExchangesOrVASPEntityInfo.from_json(json)
# print the JSON string representation of the object
print(TravelRuleWithdrawExchangesOrVASPEntityInfo.to_json())

# convert the object into a dict
travel_rule_withdraw_exchanges_or_vasp_entity_info_dict = travel_rule_withdraw_exchanges_or_vasp_entity_info_instance.to_dict()
# create an instance of TravelRuleWithdrawExchangesOrVASPEntityInfo from a dict
travel_rule_withdraw_exchanges_or_vasp_entity_info_from_dict = TravelRuleWithdrawExchangesOrVASPEntityInfo.from_dict(travel_rule_withdraw_exchanges_or_vasp_entity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


