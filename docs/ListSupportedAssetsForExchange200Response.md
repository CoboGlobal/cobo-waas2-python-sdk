# ListSupportedAssetsForExchange200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AssetInfo]**](AssetInfo.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_supported_assets_for_exchange200_response import ListSupportedAssetsForExchange200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportedAssetsForExchange200Response from a JSON string
list_supported_assets_for_exchange200_response_instance = ListSupportedAssetsForExchange200Response.from_json(json)
# print the JSON string representation of the object
print(ListSupportedAssetsForExchange200Response.to_json())

# convert the object into a dict
list_supported_assets_for_exchange200_response_dict = list_supported_assets_for_exchange200_response_instance.to_dict()
# create an instance of ListSupportedAssetsForExchange200Response from a dict
list_supported_assets_for_exchange200_response_from_dict = ListSupportedAssetsForExchange200Response.from_dict(list_supported_assets_for_exchange200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


