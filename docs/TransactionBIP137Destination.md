# TransactionBIP137Destination

The information about the destination `BTC_BIP_137`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**message_bip137** | **str** | Message to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.transaction_bip137_destination import TransactionBIP137Destination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBIP137Destination from a JSON string
transaction_bip137_destination_instance = TransactionBIP137Destination.from_json(json)
# print the JSON string representation of the object
print(TransactionBIP137Destination.to_json())

# convert the object into a dict
transaction_bip137_destination_dict = transaction_bip137_destination_instance.to_dict()
# create an instance of TransactionBIP137Destination from a dict
transaction_bip137_destination_from_dict = TransactionBIP137Destination.from_dict(transaction_bip137_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


