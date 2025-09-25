# SolContractCallDestination

The information about the transaction destination. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**ContractCallDestinationType**](ContractCallDestinationType.md) |  | 
**instructions** | [**List[SolContractCallInstruction]**](SolContractCallInstruction.md) |  | 
**address_lookup_table_accounts** | [**List[SolContractCallAddressLookupTableAccount]**](SolContractCallAddressLookupTableAccount.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.sol_contract_call_destination import SolContractCallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of SolContractCallDestination from a JSON string
sol_contract_call_destination_instance = SolContractCallDestination.from_json(json)
# print the JSON string representation of the object
print(SolContractCallDestination.to_json())

# convert the object into a dict
sol_contract_call_destination_dict = sol_contract_call_destination_instance.to_dict()
# create an instance of SolContractCallDestination from a dict
sol_contract_call_destination_from_dict = SolContractCallDestination.from_dict(sol_contract_call_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


