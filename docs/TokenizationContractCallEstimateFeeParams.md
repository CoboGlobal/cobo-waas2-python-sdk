# TokenizationContractCallEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | [optional] 
**data** | [**TokenizationContractCallParamsData**](TokenizationContractCallParamsData.md) |  | [optional] 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**token_id** | **str** | The ID of the token. | 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_contract_call_estimate_fee_params import TokenizationContractCallEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationContractCallEstimateFeeParams from a JSON string
tokenization_contract_call_estimate_fee_params_instance = TokenizationContractCallEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationContractCallEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_contract_call_estimate_fee_params_dict = tokenization_contract_call_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationContractCallEstimateFeeParams from a dict
tokenization_contract_call_estimate_fee_params_from_dict = TokenizationContractCallEstimateFeeParams.from_dict(tokenization_contract_call_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


