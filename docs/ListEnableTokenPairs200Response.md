# ListEnableTokenPairs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SwapTokenPair]**](SwapTokenPair.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_enable_token_pairs200_response import ListEnableTokenPairs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListEnableTokenPairs200Response from a JSON string
list_enable_token_pairs200_response_instance = ListEnableTokenPairs200Response.from_json(json)
# print the JSON string representation of the object
print(ListEnableTokenPairs200Response.to_json())

# convert the object into a dict
list_enable_token_pairs200_response_dict = list_enable_token_pairs200_response_instance.to_dict()
# create an instance of ListEnableTokenPairs200Response from a dict
list_enable_token_pairs200_response_from_dict = ListEnableTokenPairs200Response.from_dict(list_enable_token_pairs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


