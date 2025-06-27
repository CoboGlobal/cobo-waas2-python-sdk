# TokenizationTokenPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_type** | [**TokenizationTokenPermissionType**](TokenizationTokenPermissionType.md) |  | 
**name** | **str** | The display name of the permission. | 
**description** | **str** | Detailed description of what this permission allows. | 
**enabled** | **bool** | Whether this permission is currently enabled. | 

## Example

```python
from cobo_waas2.models.tokenization_token_permission import TokenizationTokenPermission

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationTokenPermission from a JSON string
tokenization_token_permission_instance = TokenizationTokenPermission.from_json(json)
# print the JSON string representation of the object
print(TokenizationTokenPermission.to_json())

# convert the object into a dict
tokenization_token_permission_dict = tokenization_token_permission_instance.to_dict()
# create an instance of TokenizationTokenPermission from a dict
tokenization_token_permission_from_dict = TokenizationTokenPermission.from_dict(tokenization_token_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


