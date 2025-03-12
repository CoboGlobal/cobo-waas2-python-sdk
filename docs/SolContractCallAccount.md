# SolContractCallAccount

The information about the account involved in a Solana instruction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | The public key of the account. If the account is a signer of this transaction, this property must be the same as the value of the &#x60;source.address&#x60; property.  | 
**is_signer** | **bool** | Whether the account is the signer of this transaction: - &#x60;true&#x60;: The account is a signer. - &#x60;false&#x60;: The account is not a signer.  | 
**is_writable** | **bool** | Whether the account can be modified by the instruction: - &#x60;true&#x60;: The account can be modified by the instruction. - &#x60;false&#x60;: The account cannot be modified by the instruction.  | 

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


