# TransactionStellarContractParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | [**TransactionStellarContractType**](TransactionStellarContractType.md) |  | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | 
**operation_type** | [**TransactionStellarTrustLineOperationType**](TransactionStellarTrustLineOperationType.md) |  | 

## Example

```python
from cobo_waas2.models.transaction_stellar_contract_param import TransactionStellarContractParam

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionStellarContractParam from a JSON string
transaction_stellar_contract_param_instance = TransactionStellarContractParam.from_json(json)
# print the JSON string representation of the object
print(TransactionStellarContractParam.to_json())

# convert the object into a dict
transaction_stellar_contract_param_dict = transaction_stellar_contract_param_instance.to_dict()
# create an instance of TransactionStellarContractParam from a dict
transaction_stellar_contract_param_from_dict = TransactionStellarContractParam.from_dict(transaction_stellar_contract_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


