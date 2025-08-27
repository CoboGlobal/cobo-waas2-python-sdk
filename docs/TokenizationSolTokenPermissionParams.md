# TokenizationSolTokenPermissionParams

Role-based permission settings for the Solana Token-2022 Program. If not provided, all permissions will be granted to the issuing wallet by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permanent_delegate** | **str** | Solana wallet address assigned as the permanent delegate authority. It can perform delegated operations on behalf of token holders. | [optional] 
**minter** | **str** | Solana wallet address assigned as the mint authority. It can mint new tokens. | [optional] 
**freezer** | **str** | Solana wallet address assigned as the freeze authority. It can freeze token accounts. | [optional] 
**updater** | **str** | Solana wallet address assigned as the update authority. It can update token metadata. | [optional] 
**pauser** | **str** | Solana wallet address assigned as the pause authority. It can pause or unpause all token activities including transfers, burns, and mints. | [optional] 

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


