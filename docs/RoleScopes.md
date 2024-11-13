# RoleScopes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | The user role associated with this API key. | 
**scopes** | [**Scopes**](Scopes.md) |  | 

## Example

```python
from cobo_waas2.models.role_scopes import RoleScopes

# TODO update the JSON string below
json = "{}"
# create an instance of RoleScopes from a JSON string
role_scopes_instance = RoleScopes.from_json(json)
# print the JSON string representation of the object
print(RoleScopes.to_json())

# convert the object into a dict
role_scopes_dict = role_scopes_instance.to_dict()
# create an instance of RoleScopes from a dict
role_scopes_from_dict = RoleScopes.from_dict(role_scopes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


