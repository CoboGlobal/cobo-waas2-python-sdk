# TransactionTronContractDestination

Information about the transaction destination type `TRON_Contract`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**address** | **str** | The destination address. | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 TRON, then the value is &#x60;1.5&#x60;.  | [optional] 
**calldata** | **str** | The data that is used to invoke a specific function or method within the specified contract at the destination address.  | 

## Example

```python
from cobo_waas2.models.transaction_tron_contract_destination import TransactionTronContractDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTronContractDestination from a JSON string
transaction_tron_contract_destination_instance = TransactionTronContractDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionTronContractDestination.to_json())

# convert the object into a dict
transaction_tron_contract_destination_dict = transaction_tron_contract_destination_instance.to_dict()
# create an instance of TransactionTronContractDestination from a dict
transaction_tron_contract_destination_from_dict = TransactionTronContractDestination.from_dict(transaction_tron_contract_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


