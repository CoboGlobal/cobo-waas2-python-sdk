# ListKeyShareHolderGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KeyShareHolderGroup]**](KeyShareHolderGroup.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_key_share_holder_groups200_response import ListKeyShareHolderGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListKeyShareHolderGroups200Response from a JSON string
list_key_share_holder_groups200_response_instance = ListKeyShareHolderGroups200Response.from_json(json)
# print the JSON string representation of the object
print(ListKeyShareHolderGroups200Response.to_json())

# convert the object into a dict
list_key_share_holder_groups200_response_dict = list_key_share_holder_groups200_response_instance.to_dict()
# create an instance of ListKeyShareHolderGroups200Response from a dict
list_key_share_holder_groups200_response_from_dict = ListKeyShareHolderGroups200Response.from_dict(list_key_share_holder_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


