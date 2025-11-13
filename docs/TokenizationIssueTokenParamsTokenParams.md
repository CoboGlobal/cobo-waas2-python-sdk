# TokenizationIssueTokenParamsTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard** | [**TokenizationTokenStandard**](TokenizationTokenStandard.md) |  | 
**name** | **str** | The name of the token. | 
**symbol** | **str** | The symbol of the token. | 
**decimals** | **int** | The number of decimals for the token (0-18). | 
**token_access_activated** | **bool** | Whether the allowlist feature is activated for the token. When activated, only addresses in the allowlist can perform token operations. | [optional] [default to False]
**permissions** | [**TokenizationSolWrappedTokenPermissionParams**](TokenizationSolWrappedTokenPermissionParams.md) |  | [optional] 
**underlying_token** | **str** | The address of the underlying token that this tokenized asset represents. | 

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


