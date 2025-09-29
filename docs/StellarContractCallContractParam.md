# StellarContractCallContractParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | [**StellarContractCallContractType**](StellarContractCallContractType.md) |  | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | 
**operation_type** | [**StellarContractCallTrustLineOperationType**](StellarContractCallTrustLineOperationType.md) |  | 

## Example

```python
from cobo_waas2.models.stellar_contract_call_contract_param import StellarContractCallContractParam

# TODO update the JSON string below
json = "{}"
# create an instance of StellarContractCallContractParam from a JSON string
stellar_contract_call_contract_param_instance = StellarContractCallContractParam.from_json(json)
# print the JSON string representation of the object
print(StellarContractCallContractParam.to_json())

# convert the object into a dict
stellar_contract_call_contract_param_dict = stellar_contract_call_contract_param_instance.to_dict()
# create an instance of StellarContractCallContractParam from a dict
stellar_contract_call_contract_param_from_dict = StellarContractCallContractParam.from_dict(stellar_contract_call_contract_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


