# SolContractCallAddressLookupTableAccount

The information about the Solana address lookup table account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_account_key** | **str** | The on-chain public key of the address lookup table account (ALT), identifying the specific lookup table. | 
**addresses** | **List[str]** | An array of stored account addresses within the lookup table, which can be referenced in the transaction by index. | 

## Example

```python
from cobo_waas2.models.sol_contract_call_address_lookup_table_account import SolContractCallAddressLookupTableAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SolContractCallAddressLookupTableAccount from a JSON string
sol_contract_call_address_lookup_table_account_instance = SolContractCallAddressLookupTableAccount.from_json(json)
# print the JSON string representation of the object
print(SolContractCallAddressLookupTableAccount.to_json())

# convert the object into a dict
sol_contract_call_address_lookup_table_account_dict = sol_contract_call_address_lookup_table_account_instance.to_dict()
# create an instance of SolContractCallAddressLookupTableAccount from a dict
sol_contract_call_address_lookup_table_account_from_dict = SolContractCallAddressLookupTableAccount.from_dict(sol_contract_call_address_lookup_table_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


