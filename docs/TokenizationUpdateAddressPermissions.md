# TokenizationUpdateAddressPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address to manage permissions for. | 
**action** | [**TokenizationPermissionAction**](TokenizationPermissionAction.md) |  | 
**permissions** | [**List[TokenizationTokenPermissionType]**](TokenizationTokenPermissionType.md) | The list of permissions to be applied. | 

## Example

```python
from cobo_waas2.models.tokenization_update_address_permissions import TokenizationUpdateAddressPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdateAddressPermissions from a JSON string
tokenization_update_address_permissions_instance = TokenizationUpdateAddressPermissions.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdateAddressPermissions.to_json())

# convert the object into a dict
tokenization_update_address_permissions_dict = tokenization_update_address_permissions_instance.to_dict()
# create an instance of TokenizationUpdateAddressPermissions from a dict
tokenization_update_address_permissions_from_dict = TokenizationUpdateAddressPermissions.from_dict(tokenization_update_address_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


