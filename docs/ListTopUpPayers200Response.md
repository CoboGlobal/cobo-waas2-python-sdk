# ListTopUpPayers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ListTopUpPayers200ResponseDataInner]**](ListTopUpPayers200ResponseDataInner.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_top_up_payers200_response import ListTopUpPayers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTopUpPayers200Response from a JSON string
list_top_up_payers200_response_instance = ListTopUpPayers200Response.from_json(json)
# print the JSON string representation of the object
print(ListTopUpPayers200Response.to_json())

# convert the object into a dict
list_top_up_payers200_response_dict = list_top_up_payers200_response_instance.to_dict()
# create an instance of ListTopUpPayers200Response from a dict
list_top_up_payers200_response_from_dict = ListTopUpPayers200Response.from_dict(list_top_up_payers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


