# TokenizationSolContractCallParams

The information about the Solana program call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TokenizationContractCallType**](TokenizationContractCallType.md) |  | [optional] 
**instructions** | [**List[SolContractCallInstruction]**](SolContractCallInstruction.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_sol_contract_call_params import TokenizationSolContractCallParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationSolContractCallParams from a JSON string
tokenization_sol_contract_call_params_instance = TokenizationSolContractCallParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationSolContractCallParams.to_json())

# convert the object into a dict
tokenization_sol_contract_call_params_dict = tokenization_sol_contract_call_params_instance.to_dict()
# create an instance of TokenizationSolContractCallParams from a dict
tokenization_sol_contract_call_params_from_dict = TokenizationSolContractCallParams.from_dict(tokenization_sol_contract_call_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


