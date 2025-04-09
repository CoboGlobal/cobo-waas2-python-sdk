# TransactionCosmosContractDestination

Information about the transaction destination type `COSMOS_Contract`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**cosmos_messages** | [**List[TransactionCosmosMessage]**](TransactionCosmosMessage.md) |  | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_cosmos_contract_destination import TransactionCosmosContractDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCosmosContractDestination from a JSON string
transaction_cosmos_contract_destination_instance = TransactionCosmosContractDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionCosmosContractDestination.to_json())

# convert the object into a dict
transaction_cosmos_contract_destination_dict = transaction_cosmos_contract_destination_instance.to_dict()
# create an instance of TransactionCosmosContractDestination from a dict
transaction_cosmos_contract_destination_from_dict = TransactionCosmosContractDestination.from_dict(transaction_cosmos_contract_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


