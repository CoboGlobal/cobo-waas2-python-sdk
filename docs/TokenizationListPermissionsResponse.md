# TokenizationListPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenizationListPermissionsResponseDataInner]**](TokenizationListPermissionsResponseDataInner.md) | List of permissions. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_list_permissions_response import TokenizationListPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationListPermissionsResponse from a JSON string
tokenization_list_permissions_response_instance = TokenizationListPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationListPermissionsResponse.to_json())

# convert the object into a dict
tokenization_list_permissions_response_dict = tokenization_list_permissions_response_instance.to_dict()
# create an instance of TokenizationListPermissionsResponse from a dict
tokenization_list_permissions_response_from_dict = TokenizationListPermissionsResponse.from_dict(tokenization_list_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


