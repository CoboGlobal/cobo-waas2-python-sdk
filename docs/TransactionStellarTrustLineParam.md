# TransactionStellarTrustLineParam

Parameters related to Stellar trustline operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | [**TransactionStellarContractType**](TransactionStellarContractType.md) |  | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | 
**operation_type** | [**TransactionStellarTrustLineOperationType**](TransactionStellarTrustLineOperationType.md) |  | 

## Example

```python
from cobo_waas2.models.transaction_stellar_trust_line_param import TransactionStellarTrustLineParam

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionStellarTrustLineParam from a JSON string
transaction_stellar_trust_line_param_instance = TransactionStellarTrustLineParam.from_json(json)
# print the JSON string representation of the object
print(TransactionStellarTrustLineParam.to_json())

# convert the object into a dict
transaction_stellar_trust_line_param_dict = transaction_stellar_trust_line_param_instance.to_dict()
# create an instance of TransactionStellarTrustLineParam from a dict
transaction_stellar_trust_line_param_from_dict = TransactionStellarTrustLineParam.from_dict(transaction_stellar_trust_line_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


