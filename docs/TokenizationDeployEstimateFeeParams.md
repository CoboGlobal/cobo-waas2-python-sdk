# TokenizationDeployEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID where the token will be issued. | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**token_params** | [**TokenizationIssueTokenParamsTokenParams**](TokenizationIssueTokenParamsTokenParams.md) |  | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_deploy_estimate_fee_params import TokenizationDeployEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationDeployEstimateFeeParams from a JSON string
tokenization_deploy_estimate_fee_params_instance = TokenizationDeployEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationDeployEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_deploy_estimate_fee_params_dict = tokenization_deploy_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationDeployEstimateFeeParams from a dict
tokenization_deploy_estimate_fee_params_from_dict = TokenizationDeployEstimateFeeParams.from_dict(tokenization_deploy_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


