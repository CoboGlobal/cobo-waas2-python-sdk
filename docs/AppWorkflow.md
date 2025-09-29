# AppWorkflow

The information of an app workflow approval user entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow id. | 
**operation_id** | **str** | The workflow operation id. | 
**operation_name** | **str** | The workflow operation name. | 
**current_policies** | [**List[AppWorkflowPolicy]**](AppWorkflowPolicy.md) |  | 

## Example

```python
from cobo_waas2.models.app_workflow import AppWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflow from a JSON string
app_workflow_instance = AppWorkflow.from_json(json)
# print the JSON string representation of the object
print(AppWorkflow.to_json())

# convert the object into a dict
app_workflow_dict = app_workflow_instance.to_dict()
# create an instance of AppWorkflow from a dict
app_workflow_from_dict = AppWorkflow.from_dict(app_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


