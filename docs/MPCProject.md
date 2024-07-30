# MPCProject

The data for project information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID. | [optional] 
**org_id** | **str** | The [organization](https://manuals.cobo.com/en/portal/organization/introduction) ID. | [optional] 
**name** | **str** | The project name. | [optional] 
**node_count** | **int** | The number of key share holders in the project. | [optional] 
**threshold** | **int** | The number of key share holders required to sign an operation in the project. | [optional] 
**create_timestamp** | **int** | The project&#39;s creation time in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.mpc_project import MPCProject

# TODO update the JSON string below
json = "{}"
# create an instance of MPCProject from a JSON string
mpc_project_instance = MPCProject.from_json(json)
# print the JSON string representation of the object
print(MPCProject.to_json())

# convert the object into a dict
mpc_project_dict = mpc_project_instance.to_dict()
# create an instance of MPCProject from a dict
mpc_project_from_dict = MPCProject.from_dict(mpc_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


