# TokenizationIssueTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID where the token will be issued. | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**token_params** | [**TokenizationIssueTokenParamsTokenParams**](TokenizationIssueTokenParamsTokenParams.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_issue_token_params import TokenizationIssueTokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationIssueTokenParams from a JSON string
tokenization_issue_token_params_instance = TokenizationIssueTokenParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationIssueTokenParams.to_json())

# convert the object into a dict
tokenization_issue_token_params_dict = tokenization_issue_token_params_instance.to_dict()
# create an instance of TokenizationIssueTokenParams from a dict
tokenization_issue_token_params_from_dict = TokenizationIssueTokenParams.from_dict(tokenization_issue_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


