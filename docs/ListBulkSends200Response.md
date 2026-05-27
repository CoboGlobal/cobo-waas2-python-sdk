# ListBulkSends200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PaymentBulkSend]**](PaymentBulkSend.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_bulk_sends200_response import ListBulkSends200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListBulkSends200Response from a JSON string
list_bulk_sends200_response_instance = ListBulkSends200Response.from_json(json)
# print the JSON string representation of the object
print(ListBulkSends200Response.to_json())

# convert the object into a dict
list_bulk_sends200_response_dict = list_bulk_sends200_response_instance.to_dict()
# create an instance of ListBulkSends200Response from a dict
list_bulk_sends200_response_from_dict = ListBulkSends200Response.from_dict(list_bulk_sends200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


