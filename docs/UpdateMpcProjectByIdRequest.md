# UpdateMpcProjectByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The project&#39;s new name. | 

## Example

```python
from cobo_waas2.models.update_mpc_project_by_id_request import UpdateMpcProjectByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMpcProjectByIdRequest from a JSON string
update_mpc_project_by_id_request_instance = UpdateMpcProjectByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMpcProjectByIdRequest.to_json())

# convert the object into a dict
update_mpc_project_by_id_request_dict = update_mpc_project_by_id_request_instance.to_dict()
# create an instance of UpdateMpcProjectByIdRequest from a dict
update_mpc_project_by_id_request_from_dict = UpdateMpcProjectByIdRequest.from_dict(update_mpc_project_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


