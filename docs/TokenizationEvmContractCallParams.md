# TokenizationEvmContractCallParams

The information about the EVM contract call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TokenizationContractCallType**](TokenizationContractCallType.md) |  | [optional] 
**calldata** | **str** | The data used to invoke a specific function or method within the specified contract at the destination address, with a maximum length of 65,000 characters.  | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_evm_contract_call_params import TokenizationEvmContractCallParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationEvmContractCallParams from a JSON string
tokenization_evm_contract_call_params_instance = TokenizationEvmContractCallParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationEvmContractCallParams.to_json())

# convert the object into a dict
tokenization_evm_contract_call_params_dict = tokenization_evm_contract_call_params_instance.to_dict()
# create an instance of TokenizationEvmContractCallParams from a dict
tokenization_evm_contract_call_params_from_dict = TokenizationEvmContractCallParams.from_dict(tokenization_evm_contract_call_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


