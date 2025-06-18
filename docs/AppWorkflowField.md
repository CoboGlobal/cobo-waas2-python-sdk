# AppWorkflowField

The information of a workflow field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The workflow field name. | 
**value_type** | [**PolicyFieldValueType**](PolicyFieldValueType.md) |  | 
**value** | **str** | The workflow field value. | 

## Example

```python
from cobo_waas2.models.app_workflow_field import AppWorkflowField

# TODO update the JSON string below
json = "{}"
# create an instance of AppWorkflowField from a JSON string
app_workflow_field_instance = AppWorkflowField.from_json(json)
# print the JSON string representation of the object
print(AppWorkflowField.to_json())

# convert the object into a dict
app_workflow_field_dict = app_workflow_field_instance.to_dict()
# create an instance of AppWorkflowField from a dict
app_workflow_field_from_dict = AppWorkflowField.from_dict(app_workflow_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


