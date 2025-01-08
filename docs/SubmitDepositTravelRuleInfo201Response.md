# SubmitDepositTravelRuleInfo201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submitted** | **bool** | Whether the submitted Travel Rule info has been successfully executed. - &#x60;true&#x60;: The operation has been successfully executed. - &#x60;false&#x60;: The operation has not been executed.  | [optional] 

## Example

```python
from cobo_waas2.models.submit_deposit_travel_rule_info201_response import SubmitDepositTravelRuleInfo201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitDepositTravelRuleInfo201Response from a JSON string
submit_deposit_travel_rule_info201_response_instance = SubmitDepositTravelRuleInfo201Response.from_json(json)
# print the JSON string representation of the object
print(SubmitDepositTravelRuleInfo201Response.to_json())

# convert the object into a dict
submit_deposit_travel_rule_info201_response_dict = submit_deposit_travel_rule_info201_response_instance.to_dict()
# create an instance of SubmitDepositTravelRuleInfo201Response from a dict
submit_deposit_travel_rule_info201_response_from_dict = SubmitDepositTravelRuleInfo201Response.from_dict(submit_deposit_travel_rule_info201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


