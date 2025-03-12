# SolContractCallInstruction

The information about the Solana instruction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[SolContractCallAccount]**](SolContractCallAccount.md) |  | 
**data** | **str** | The Base64-encoded instruction data used for interacting with a Solana program.  | 
**program_id** | **str** | The address of the Solana program (smart contract).   | 

## Example

```python
from cobo_waas2.models.sol_contract_call_instruction import SolContractCallInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of SolContractCallInstruction from a JSON string
sol_contract_call_instruction_instance = SolContractCallInstruction.from_json(json)
# print the JSON string representation of the object
print(SolContractCallInstruction.to_json())

# convert the object into a dict
sol_contract_call_instruction_dict = sol_contract_call_instruction_instance.to_dict()
# create an instance of SolContractCallInstruction from a dict
sol_contract_call_instruction_from_dict = SolContractCallInstruction.from_dict(sol_contract_call_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


