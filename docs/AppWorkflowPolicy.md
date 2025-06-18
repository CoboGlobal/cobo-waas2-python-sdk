# AppWorkflowPolicy

The current approval workflow policy, consisting of one or more conditions and an associated action. When the conditions are met, the action is triggered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**PolicyAction**](PolicyAction.md) |  | 
**conditions** | [**List[PolicyCondition]**](PolicyCondition.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.app_workflow_policy import AppWorkflowPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflowPolicy from a JSON string
app_workflow_policy_instance = AppWorkflowPolicy.from_json(json)
# print the JSON string representation of the object
print(AppWorkflowPolicy.to_json())

# convert the object into a dict
app_workflow_policy_dict = app_workflow_policy_instance.to_dict()
# create an instance of AppWorkflowPolicy from a dict
app_workflow_policy_from_dict = AppWorkflowPolicy.from_dict(app_workflow_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


