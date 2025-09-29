# TokenizationERC20WrappedTokenPermissionParams

Role-based permission settings for token contract. If not provided, all permissions will be granted to the issuance wallet by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **List[str]** | List of addresses for the admin role. | [optional] 
**minter** | **List[str]** | List of addresses for the minter role. | [optional] 
**wrapper** | **List[str]** | List of addresses for the wrapper role. | [optional] 
**manager** | **List[str]** | List of addresses for the manager role. | [optional] 
**pauser** | **List[str]** | List of addresses for the pauser role. | [optional] 
**salvager** | **List[str]** | List of addresses for the salvager role. | [optional] 
**upgrader** | **List[str]** | List of addresses for the upgrader role. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_erc20_wrapped_token_permission_params import TokenizationERC20WrappedTokenPermissionParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationERC20WrappedTokenPermissionParams from a JSON string
tokenization_erc20_wrapped_token_permission_params_instance = TokenizationERC20WrappedTokenPermissionParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationERC20WrappedTokenPermissionParams.to_json())

# convert the object into a dict
tokenization_erc20_wrapped_token_permission_params_dict = tokenization_erc20_wrapped_token_permission_params_instance.to_dict()
# create an instance of TokenizationERC20WrappedTokenPermissionParams from a dict
tokenization_erc20_wrapped_token_permission_params_from_dict = TokenizationERC20WrappedTokenPermissionParams.from_dict(tokenization_erc20_wrapped_token_permission_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


