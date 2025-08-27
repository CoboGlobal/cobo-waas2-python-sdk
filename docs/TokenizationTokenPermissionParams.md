# TokenizationTokenPermissionParams

Role-based permission settings for token contract. If not provided, all permissions will be granted to the issuing wallet by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **List[str]** | List of addresses for the admin role. | [optional] 
**minter** | **List[str]** | List of addresses for the minter role. | [optional] 
**burner** | **List[str]** | List of addresses for the burner role. | [optional] 
**manager** | **List[str]** | List of addresses for the manager role. | [optional] 
**pauser** | **List[str]** | List of addresses for the pauser role. | [optional] 
**salvager** | **List[str]** | List of addresses for the salvager role. | [optional] 
**upgrader** | **List[str]** | List of addresses for the upgrader role. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_token_permission_params import TokenizationTokenPermissionParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationTokenPermissionParams from a JSON string
tokenization_token_permission_params_instance = TokenizationTokenPermissionParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationTokenPermissionParams.to_json())

# convert the object into a dict
tokenization_token_permission_params_dict = tokenization_token_permission_params_instance.to_dict()
# create an instance of TokenizationTokenPermissionParams from a dict
tokenization_token_permission_params_from_dict = TokenizationTokenPermissionParams.from_dict(tokenization_token_permission_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


