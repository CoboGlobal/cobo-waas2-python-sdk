# TransactionSolContractAddressLookupTableAccount

The information about the Solana address lookup table account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_account_key** | **str** | The on-chain public key of the address lookup table account (ALT), identifying the specific lookup table. | 
**addresses** | **List[str]** | An array of stored account addresses within the lookup table, which can be referenced in the transaction by index. | 

## Example

```python
from cobo_waas2.models.transaction_sol_contract_address_lookup_table_account import TransactionSolContractAddressLookupTableAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSolContractAddressLookupTableAccount from a JSON string
transaction_sol_contract_address_lookup_table_account_instance = TransactionSolContractAddressLookupTableAccount.from_json(json)
# print the JSON string representation of the object
print(TransactionSolContractAddressLookupTableAccount.to_json())

# convert the object into a dict
transaction_sol_contract_address_lookup_table_account_dict = transaction_sol_contract_address_lookup_table_account_instance.to_dict()
# create an instance of TransactionSolContractAddressLookupTableAccount from a dict
transaction_sol_contract_address_lookup_table_account_from_dict = TransactionSolContractAddressLookupTableAccount.from_dict(transaction_sol_contract_address_lookup_table_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


