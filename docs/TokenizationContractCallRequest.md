# TokenizationContractCallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | [optional] 
**data** | [**TokenizationContractCallParamsData**](TokenizationContractCallParamsData.md) |  | [optional] 
**app_initiator** | **str** | The initiator of the tokenization activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_contract_call_request import TokenizationContractCallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationContractCallRequest from a JSON string
tokenization_contract_call_request_instance = TokenizationContractCallRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationContractCallRequest.to_json())

# convert the object into a dict
tokenization_contract_call_request_dict = tokenization_contract_call_request_instance.to_dict()
# create an instance of TokenizationContractCallRequest from a dict
tokenization_contract_call_request_from_dict = TokenizationContractCallRequest.from_dict(tokenization_contract_call_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


