# ListAutoSweepTask200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AutoSweepTask]**](AutoSweepTask.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_auto_sweep_task200_response import ListAutoSweepTask200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAutoSweepTask200Response from a JSON string
list_auto_sweep_task200_response_instance = ListAutoSweepTask200Response.from_json(json)
# print the JSON string representation of the object
print(ListAutoSweepTask200Response.to_json())

# convert the object into a dict
list_auto_sweep_task200_response_dict = list_auto_sweep_task200_response_instance.to_dict()
# create an instance of ListAutoSweepTask200Response from a dict
list_auto_sweep_task200_response_from_dict = ListAutoSweepTask200Response.from_dict(list_auto_sweep_task200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


