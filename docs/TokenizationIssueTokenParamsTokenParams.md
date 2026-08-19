# TokenizationIssueTokenParamsTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard** | [**TokenizationTokenStandard**](TokenizationTokenStandard.md) |  | 
**name** | **str** | The name of the fund token. | 
**symbol** | **str** | The symbol of the fund token. | 
**decimals** | **int** | The number of decimals for the token (0-18). | 
**token_access_activated** | **bool** | Whether the allowlist feature is activated for the token. When activated, only addresses in the allowlist can perform token operations. | [optional] [default to False]
**permissions** | [**TokenizationERC20FundTokenPermissionParams**](TokenizationERC20FundTokenPermissionParams.md) |  | [optional] 
**underlying_token** | **str** | The address of the underlying token that this tokenized asset represents. | 
**asset_token** | **str** | The address of the underlying asset token (e.g., XAUT, USDC). The fund will hold this token as collateral. | 
**initial_nav** | **str** | Initial net asset value (NAV) per share (optional). Default: &#39;1.0&#39; (standard for new funds). | [optional] [default to '1.0']
**initial_annual_rate** | **str** | Initial annual rate (optional). Can be updated later via NAV updater. Default: &#39;0&#39;. | [optional] [default to '0']
**min_deposit** | **str** | Minimum deposit amount (optional). Default: &#39;0&#39; (no minimum, accepts any amount &gt; 0). Admin can update this later. | [optional] [default to '0']
**min_redemption** | **str** | Minimum redemption amount (optional). Default: &#39;0&#39; (no minimum, accepts any amount &gt; 0). Admin can update this later. | [optional] [default to '0']
**max_annual_rate** | **str** | Maximum allowed annual rate (optional). Default: type(uint256).max (no limit). Set lower for conservative funds (e.g., &#39;0.2&#39; for 20%). | [optional] [default to '115792089237316195423570985008687907853269984665640564039457584007913129639935']
**max_rate_change** | **str** | Maximum rate change per NAV update (optional). Default: type(uint256).max (no limit). Set lower to prevent volatility (e.g., &#39;0.05&#39; for 5%). | [optional] [default to '115792089237316195423570985008687907853269984665640564039457584007913129639935']
**min_update_interval_seconds** | **int** | Minimum interval between NAV updates in seconds (optional). Default: 0 (no minimum). Set higher to prevent frequent updates (e.g., 86400 for 1 day). | [optional] [default to 0]

## Example

```python
from cobo_waas2.models.tokenization_issue_token_params_token_params import TokenizationIssueTokenParamsTokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationIssueTokenParamsTokenParams from a JSON string
tokenization_issue_token_params_token_params_instance = TokenizationIssueTokenParamsTokenParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationIssueTokenParamsTokenParams.to_json())

# convert the object into a dict
tokenization_issue_token_params_token_params_dict = tokenization_issue_token_params_token_params_instance.to_dict()
# create an instance of TokenizationIssueTokenParamsTokenParams from a dict
tokenization_issue_token_params_token_params_from_dict = TokenizationIssueTokenParamsTokenParams.from_dict(tokenization_issue_token_params_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


