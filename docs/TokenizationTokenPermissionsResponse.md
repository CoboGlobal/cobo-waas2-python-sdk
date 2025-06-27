# TokenizationTokenPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[TokenizationTokenPermission]**](TokenizationTokenPermission.md) | List of available token permissions. | 
**total_count** | **int** | Total number of permissions. | 

## Example

```python
from cobo_waas2.models.tokenization_token_permissions_response import TokenizationTokenPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationTokenPermissionsResponse from a JSON string
tokenization_token_permissions_response_instance = TokenizationTokenPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationTokenPermissionsResponse.to_json())

# convert the object into a dict
tokenization_token_permissions_response_dict = tokenization_token_permissions_response_instance.to_dict()
# create an instance of TokenizationTokenPermissionsResponse from a dict
tokenization_token_permissions_response_from_dict = TokenizationTokenPermissionsResponse.from_dict(tokenization_token_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


