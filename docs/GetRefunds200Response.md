# GetRefunds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Refund]**](Refund.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.get_refunds200_response import GetRefunds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefunds200Response from a JSON string
get_refunds200_response_instance = GetRefunds200Response.from_json(json)
# print the JSON string representation of the object
print(GetRefunds200Response.to_json())

# convert the object into a dict
get_refunds200_response_dict = get_refunds200_response_instance.to_dict()
# create an instance of GetRefunds200Response from a dict
get_refunds200_response_from_dict = GetRefunds200Response.from_dict(get_refunds200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


