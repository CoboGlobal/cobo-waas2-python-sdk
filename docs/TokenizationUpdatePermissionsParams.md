# TokenizationUpdatePermissionsParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**addresses** | [**List[TokenizationUpdateAddressPermissions]**](TokenizationUpdateAddressPermissions.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_update_permissions_params import TokenizationUpdatePermissionsParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdatePermissionsParams from a JSON string
tokenization_update_permissions_params_instance = TokenizationUpdatePermissionsParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdatePermissionsParams.to_json())

# convert the object into a dict
tokenization_update_permissions_params_dict = tokenization_update_permissions_params_instance.to_dict()
# create an instance of TokenizationUpdatePermissionsParams from a dict
tokenization_update_permissions_params_from_dict = TokenizationUpdatePermissionsParams.from_dict(tokenization_update_permissions_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


