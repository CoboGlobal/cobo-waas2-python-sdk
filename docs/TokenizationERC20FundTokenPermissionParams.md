# TokenizationERC20FundTokenPermissionParams

Role-based permission settings for ERC-4626 fund token contract. If not provided, all permissions will be granted to the issuance wallet by default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **List[str]** | List of addresses for the owner/admin role. Have full administrative control over the fund contract. | [optional] 
**manager** | **List[str]** | List of addresses for the fund manager role. Can manage fund configurations and operational parameters. | [optional] 
**nav_updater** | **List[str]** | List of addresses for the NAV updater role. Can update the net asset value (NAV) per share price. | [optional] 
**redemption_approver** | **List[str]** | List of addresses for the redemption approver role. Can approve or reject investor redemption requests. | [optional] 
**settlement_operator** | **List[str]** | List of addresses for the settlement operator role. Can execute investment and redemption settlement operations. | [optional] 
**emergency_guardian** | **List[str]** | List of addresses for the emergency guardian role. Can trigger emergency actions such as pausing the fund. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_erc20_fund_token_permission_params import TokenizationERC20FundTokenPermissionParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationERC20FundTokenPermissionParams from a JSON string
tokenization_erc20_fund_token_permission_params_instance = TokenizationERC20FundTokenPermissionParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationERC20FundTokenPermissionParams.to_json())

# convert the object into a dict
tokenization_erc20_fund_token_permission_params_dict = tokenization_erc20_fund_token_permission_params_instance.to_dict()
# create an instance of TokenizationERC20FundTokenPermissionParams from a dict
tokenization_erc20_fund_token_permission_params_from_dict = TokenizationERC20FundTokenPermissionParams.from_dict(tokenization_erc20_fund_token_permission_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


