# TransactionEvmContractMethod

The information about a method in a smart contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The method name. | [optional] 
**sig** | **str** | The signature of the method, which includes the method name and parameter types. | [optional] 
**type** | **str** | The method type. | [optional] 
**payable** | **bool** | Whether the method is payable, which means it can receive tokens along with the transaction. - &#x60;true&#x60;: The method is payable. - &#x60;false&#x60;: The method is not payable.  | [optional] 
**selector** | **str** | The method selector, a four-byte identifier derived from the method&#39;s signature, used to invoke the method in a transaction. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_evm_contract_method import TransactionEvmContractMethod

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEvmContractMethod from a JSON string
transaction_evm_contract_method_instance = TransactionEvmContractMethod.from_json(json)
# print the JSON string representation of the object
print(TransactionEvmContractMethod.to_json())

# convert the object into a dict
transaction_evm_contract_method_dict = transaction_evm_contract_method_instance.to_dict()
# create an instance of TransactionEvmContractMethod from a dict
transaction_evm_contract_method_from_dict = TransactionEvmContractMethod.from_dict(transaction_evm_contract_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


