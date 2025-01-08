# TravelRuleDepositRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | 
**travel_rule_info** | [**TravelRuleDepositRequestTravelRuleInfo**](TravelRuleDepositRequestTravelRuleInfo.md) |  | 

## Example

```python
from cobo_waas2.models.travel_rule_deposit_request import TravelRuleDepositRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleDepositRequest from a JSON string
travel_rule_deposit_request_instance = TravelRuleDepositRequest.from_json(json)
# print the JSON string representation of the object
print(TravelRuleDepositRequest.to_json())

# convert the object into a dict
travel_rule_deposit_request_dict = travel_rule_deposit_request_instance.to_dict()
# create an instance of TravelRuleDepositRequest from a dict
travel_rule_deposit_request_from_dict = TravelRuleDepositRequest.from_dict(travel_rule_deposit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


