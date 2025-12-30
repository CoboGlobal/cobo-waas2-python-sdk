# DeleteDestinationEntry200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_destination_entry_id** | **str** | The deleted destination entry ID. | 

## Example

```python
from cobo_waas2.models.delete_destination_entry200_response import DeleteDestinationEntry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDestinationEntry200Response from a JSON string
delete_destination_entry200_response_instance = DeleteDestinationEntry200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteDestinationEntry200Response.to_json())

# convert the object into a dict
delete_destination_entry200_response_dict = delete_destination_entry200_response_instance.to_dict()
# create an instance of DeleteDestinationEntry200Response from a dict
delete_destination_entry200_response_from_dict = DeleteDestinationEntry200Response.from_dict(delete_destination_entry200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


