# TransactionSolContractInstruction

sol contract instruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[TransactionSolContractAccount]**](TransactionSolContractAccount.md) |  | [optional] 
**data** | **str** | data used for calling Solana contract..  | [optional] 
**program_id** | **str** | contract address. when calling a Solana contract, the to_address parameter needs to match the program_id parameter. If multiple contracts are being called, then the to_address parameter should match the program_id parameter of the first instruction.  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_sol_contract_instruction import TransactionSolContractInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSolContractInstruction from a JSON string
transaction_sol_contract_instruction_instance = TransactionSolContractInstruction.from_json(json)
# print the JSON string representation of the object
print(TransactionSolContractInstruction.to_json())

# convert the object into a dict
transaction_sol_contract_instruction_dict = transaction_sol_contract_instruction_instance.to_dict()
# create an instance of TransactionSolContractInstruction from a dict
transaction_sol_contract_instruction_from_dict = TransactionSolContractInstruction.from_dict(transaction_sol_contract_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


