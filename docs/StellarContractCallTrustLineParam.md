# StellarContractCallTrustLineParam

Parameters related to Stellar trustline operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | [**StellarContractCallContractType**](StellarContractCallContractType.md) |  | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | 
**operation_type** | [**StellarContractCallTrustLineOperationType**](StellarContractCallTrustLineOperationType.md) |  | 

## Example

```python
from cobo_waas2.models.stellar_contract_call_trust_line_param import StellarContractCallTrustLineParam

# TODO update the JSON string below
json = "{}"
# create an instance of StellarContractCallTrustLineParam from a JSON string
stellar_contract_call_trust_line_param_instance = StellarContractCallTrustLineParam.from_json(json)
# print the JSON string representation of the object
print(StellarContractCallTrustLineParam.to_json())

# convert the object into a dict
stellar_contract_call_trust_line_param_dict = stellar_contract_call_trust_line_param_instance.to_dict()
# create an instance of StellarContractCallTrustLineParam from a dict
stellar_contract_call_trust_line_param_from_dict = StellarContractCallTrustLineParam.from_dict(stellar_contract_call_trust_line_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


