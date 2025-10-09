# TokenizationSolWrappedTokenPermissionParams

Role-based permission settings for Solana wrapped token. The owner is automatically set to the address that calls the initialize function (typically the issuance wallet) and cannot be specified here. Only wrapper and pauser roles can be configured during initialization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wrapper** | **List[str]** | List of Solana wallet addresses that can perform wrap/unwrap operations. Multiple addresses can be assigned this role. | [optional] 
**pauser** | **List[str]** | List of Solana wallet addresses that can pause/unpause the contract. Multiple addresses can be assigned this role. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_sol_wrapped_token_permission_params import TokenizationSolWrappedTokenPermissionParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationSolWrappedTokenPermissionParams from a JSON string
tokenization_sol_wrapped_token_permission_params_instance = TokenizationSolWrappedTokenPermissionParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationSolWrappedTokenPermissionParams.to_json())

# convert the object into a dict
tokenization_sol_wrapped_token_permission_params_dict = tokenization_sol_wrapped_token_permission_params_instance.to_dict()
# create an instance of TokenizationSolWrappedTokenPermissionParams from a dict
tokenization_sol_wrapped_token_permission_params_from_dict = TokenizationSolWrappedTokenPermissionParams.from_dict(tokenization_sol_wrapped_token_permission_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


