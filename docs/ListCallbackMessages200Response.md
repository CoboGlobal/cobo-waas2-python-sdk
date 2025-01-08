# ListCallbackMessages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CallbackMessage]**](CallbackMessage.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.list_callback_messages200_response import ListCallbackMessages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCallbackMessages200Response from a JSON string
list_callback_messages200_response_instance = ListCallbackMessages200Response.from_json(json)
# print the JSON string representation of the object
print(ListCallbackMessages200Response.to_json())

# convert the object into a dict
list_callback_messages200_response_dict = list_callback_messages200_response_instance.to_dict()
# create an instance of ListCallbackMessages200Response from a dict
list_callback_messages200_response_from_dict = ListCallbackMessages200Response.from_dict(list_callback_messages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


