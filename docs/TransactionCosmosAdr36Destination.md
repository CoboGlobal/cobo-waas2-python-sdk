# TransactionCosmosAdr36Destination

The information about the destination `COSMOS_ADR_36_Signature`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**message_cosmos_adr36** | **str** | Message to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.transaction_cosmos_adr36_destination import TransactionCosmosAdr36Destination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCosmosAdr36Destination from a JSON string
transaction_cosmos_adr36_destination_instance = TransactionCosmosAdr36Destination.from_json(json)
# print the JSON string representation of the object
print(TransactionCosmosAdr36Destination.to_json())

# convert the object into a dict
transaction_cosmos_adr36_destination_dict = transaction_cosmos_adr36_destination_instance.to_dict()
# create an instance of TransactionCosmosAdr36Destination from a dict
transaction_cosmos_adr36_destination_from_dict = TransactionCosmosAdr36Destination.from_dict(transaction_cosmos_adr36_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


