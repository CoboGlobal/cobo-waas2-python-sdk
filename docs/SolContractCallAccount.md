# SolContractCallAccount

sol contract instruction account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | account address. If the account is signer, pubkey needs to match the from_address parameter.  | 
**is_signer** | **bool** | boolean value indicating whether the account can sign transactions.  | 
**is_writable** | **bool** | boolean value indicating whether the account can be modified.  | 

## Example

```python
from cobo_waas2.models.sol_contract_call_account import SolContractCallAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SolContractCallAccount from a JSON string
sol_contract_call_account_instance = SolContractCallAccount.from_json(json)
# print the JSON string representation of the object
print(SolContractCallAccount.to_json())

# convert the object into a dict
sol_contract_call_account_dict = sol_contract_call_account_instance.to_dict()
# create an instance of SolContractCallAccount from a dict
sol_contract_call_account_from_dict = SolContractCallAccount.from_dict(sol_contract_call_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


