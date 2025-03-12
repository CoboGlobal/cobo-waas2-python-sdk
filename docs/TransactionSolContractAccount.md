# TransactionSolContractAccount

sol contract instruction account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | account address. If the account is signer, pubkey needs to match the from_address parameter.  | [optional] 
**is_signer** | **bool** | boolean value indicating whether the account can sign transactions.  | [optional] 
**is_writable** | **bool** | boolean value indicating whether the account can be modified.  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_sol_contract_account import TransactionSolContractAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSolContractAccount from a JSON string
transaction_sol_contract_account_instance = TransactionSolContractAccount.from_json(json)
# print the JSON string representation of the object
print(TransactionSolContractAccount.to_json())

# convert the object into a dict
transaction_sol_contract_account_dict = transaction_sol_contract_account_instance.to_dict()
# create an instance of TransactionSolContractAccount from a dict
transaction_sol_contract_account_from_dict = TransactionSolContractAccount.from_dict(transaction_sol_contract_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


