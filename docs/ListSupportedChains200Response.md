# ListSupportedChains200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ChainInfo]**](ChainInfo.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_supported_chains200_response import ListSupportedChains200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportedChains200Response from a JSON string
list_supported_chains200_response_instance = ListSupportedChains200Response.from_json(json)
# print the JSON string representation of the object
print(ListSupportedChains200Response.to_json())

# convert the object into a dict
list_supported_chains200_response_dict = list_supported_chains200_response_instance.to_dict()
# create an instance of ListSupportedChains200Response from a dict
list_supported_chains200_response_from_dict = ListSupportedChains200Response.from_dict(list_supported_chains200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


