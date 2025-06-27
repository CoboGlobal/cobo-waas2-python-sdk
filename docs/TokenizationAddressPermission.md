# TokenizationAddressPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_address** | **str** | The execution address. | 
**permissions** | [**List[TokenizationTokenPermissionType]**](TokenizationTokenPermissionType.md) | List of permissions granted to this address. | 
**created_timestamp** | **int** | The time when the permission was created, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_address_permission import TokenizationAddressPermission

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationAddressPermission from a JSON string
tokenization_address_permission_instance = TokenizationAddressPermission.from_json(json)
# print the JSON string representation of the object
print(TokenizationAddressPermission.to_json())

# convert the object into a dict
tokenization_address_permission_dict = tokenization_address_permission_instance.to_dict()
# create an instance of TokenizationAddressPermission from a dict
tokenization_address_permission_from_dict = TokenizationAddressPermission.from_dict(tokenization_address_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


