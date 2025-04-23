# TransactionSolContractDestination

The information about the transaction destination type `SOL_Contract`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**instructions** | [**List[TransactionSolContractInstruction]**](TransactionSolContractInstruction.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_sol_contract_destination import TransactionSolContractDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSolContractDestination from a JSON string
transaction_sol_contract_destination_instance = TransactionSolContractDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionSolContractDestination.to_json())

# convert the object into a dict
transaction_sol_contract_destination_dict = transaction_sol_contract_destination_instance.to_dict()
# create an instance of TransactionSolContractDestination from a dict
transaction_sol_contract_destination_from_dict = TransactionSolContractDestination.from_dict(transaction_sol_contract_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


