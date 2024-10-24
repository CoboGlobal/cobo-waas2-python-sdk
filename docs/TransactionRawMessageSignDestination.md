# TransactionRawMessageSignDestination

The information about the destination `Raw_Message_Signature`. Refer to [Transaction sources and destinations](/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**msg_hash** | **str** | Message hash to be signed, in hexadecimal format. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_raw_message_sign_destination import TransactionRawMessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRawMessageSignDestination from a JSON string
transaction_raw_message_sign_destination_instance = TransactionRawMessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionRawMessageSignDestination.to_json())

# convert the object into a dict
transaction_raw_message_sign_destination_dict = transaction_raw_message_sign_destination_instance.to_dict()
# create an instance of TransactionRawMessageSignDestination from a dict
transaction_raw_message_sign_destination_from_dict = TransactionRawMessageSignDestination.from_dict(transaction_raw_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


