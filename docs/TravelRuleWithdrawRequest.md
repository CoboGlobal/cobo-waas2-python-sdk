# TravelRuleWithdrawRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | 
**travel_rule_info** | [**TravelRuleWithdrawRequestTravelRuleInfo**](TravelRuleWithdrawRequestTravelRuleInfo.md) |  | 

## Example

```python
from cobo_waas2.models.travel_rule_withdraw_request import TravelRuleWithdrawRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleWithdrawRequest from a JSON string
travel_rule_withdraw_request_instance = TravelRuleWithdrawRequest.from_json(json)
# print the JSON string representation of the object
print(TravelRuleWithdrawRequest.to_json())

# convert the object into a dict
travel_rule_withdraw_request_dict = travel_rule_withdraw_request_instance.to_dict()
# create an instance of TravelRuleWithdrawRequest from a dict
travel_rule_withdraw_request_from_dict = TravelRuleWithdrawRequest.from_dict(travel_rule_withdraw_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


