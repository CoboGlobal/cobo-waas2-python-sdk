# TokenizationSolTokenPermissionParams

Role-based permission settings for Solana SPL Token 2022. If not provided, all permissions will be granted to the issuance wallet by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permanent_delegate** | **str** | Solana wallet address that acts as a permanent delegate authority for the token. This authority can perform delegated operations on behalf of token holders. | [optional] 
**minter** | **str** | Solana wallet addres that acts as a minter authority for the token. This authority can mint new tokens. | [optional] 
**freezer** | **str** | Solana wallet address that acts as a freezer authority for the token. This authority can freeze token accounts. | [optional] 
**updater** | **str** | Solana wallet address that acts as an updater authority for the token. This authority can update token metadata. | [optional] 
**pauser** | **str** | Solana wallet address that acts as a pauser authority for the token. This authority can pause token transfers. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_sol_token_permission_params import TokenizationSolTokenPermissionParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationSolTokenPermissionParams from a JSON string
tokenization_sol_token_permission_params_instance = TokenizationSolTokenPermissionParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationSolTokenPermissionParams.to_json())

# convert the object into a dict
tokenization_sol_token_permission_params_dict = tokenization_sol_token_permission_params_instance.to_dict()
# create an instance of TokenizationSolTokenPermissionParams from a dict
tokenization_sol_token_permission_params_from_dict = TokenizationSolTokenPermissionParams.from_dict(tokenization_sol_token_permission_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


