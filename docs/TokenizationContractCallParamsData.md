# TokenizationContractCallParamsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TokenizationContractCallType**](TokenizationContractCallType.md) |  | [optional] 
**calldata** | **str** | The data that is used to invoke a specific function or method within the specified contract at the destination address.  | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_contract_call_params_data import TokenizationContractCallParamsData

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationContractCallParamsData from a JSON string
tokenization_contract_call_params_data_instance = TokenizationContractCallParamsData.from_json(json)
# print the JSON string representation of the object
print(TokenizationContractCallParamsData.to_json())

# convert the object into a dict
tokenization_contract_call_params_data_dict = tokenization_contract_call_params_data_instance.to_dict()
# create an instance of TokenizationContractCallParamsData from a dict
tokenization_contract_call_params_data_from_dict = TokenizationContractCallParamsData.from_dict(tokenization_contract_call_params_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


