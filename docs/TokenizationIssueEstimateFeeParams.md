# TokenizationIssueEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID where the token will be issued. | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**token_params** | [**TokenizationIssueTokenParamsTokenParams**](TokenizationIssueTokenParamsTokenParams.md) |  | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_issue_estimate_fee_params import TokenizationIssueEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationIssueEstimateFeeParams from a JSON string
tokenization_issue_estimate_fee_params_instance = TokenizationIssueEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationIssueEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_issue_estimate_fee_params_dict = tokenization_issue_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationIssueEstimateFeeParams from a dict
tokenization_issue_estimate_fee_params_from_dict = TokenizationIssueEstimateFeeParams.from_dict(tokenization_issue_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


