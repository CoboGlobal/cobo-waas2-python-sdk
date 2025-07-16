# TokenizationContractCallParams

The information about the contract call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | [optional] 
**data** | [**TokenizationContractCallParamsData**](TokenizationContractCallParamsData.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_contract_call_params import TokenizationContractCallParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationContractCallParams from a JSON string
tokenization_contract_call_params_instance = TokenizationContractCallParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationContractCallParams.to_json())

# convert the object into a dict
tokenization_contract_call_params_dict = tokenization_contract_call_params_instance.to_dict()
# create an instance of TokenizationContractCallParams from a dict
tokenization_contract_call_params_from_dict = TokenizationContractCallParams.from_dict(tokenization_contract_call_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


