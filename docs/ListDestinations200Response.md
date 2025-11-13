# ListDestinations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Destination]**](Destination.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_destinations200_response import ListDestinations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDestinations200Response from a JSON string
list_destinations200_response_instance = ListDestinations200Response.from_json(json)
# print the JSON string representation of the object
print(ListDestinations200Response.to_json())

# convert the object into a dict
list_destinations200_response_dict = list_destinations200_response_instance.to_dict()
# create an instance of ListDestinations200Response from a dict
list_destinations200_response_from_dict = ListDestinations200Response.from_dict(list_destinations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


