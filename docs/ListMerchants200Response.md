# ListMerchants200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Merchant]**](Merchant.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_merchants200_response import ListMerchants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMerchants200Response from a JSON string
list_merchants200_response_instance = ListMerchants200Response.from_json(json)
# print the JSON string representation of the object
print(ListMerchants200Response.to_json())

# convert the object into a dict
list_merchants200_response_dict = list_merchants200_response_instance.to_dict()
# create an instance of ListMerchants200Response from a dict
list_merchants200_response_from_dict = ListMerchants200Response.from_dict(list_merchants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


