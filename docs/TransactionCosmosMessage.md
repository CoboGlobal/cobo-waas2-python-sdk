# TransactionCosmosMessage

The information about the Cosmos message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_url** | **str** | The type URL of the Cosmos message.  | 
**message** | **str** | The Base64-encoded Cosmos message.  | 

## Example

```python
from cobo_waas2.models.transaction_cosmos_message import TransactionCosmosMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCosmosMessage from a JSON string
transaction_cosmos_message_instance = TransactionCosmosMessage.from_json(json)
# print the JSON string representation of the object
print(TransactionCosmosMessage.to_json())

# convert the object into a dict
transaction_cosmos_message_dict = transaction_cosmos_message_instance.to_dict()
# create an instance of TransactionCosmosMessage from a dict
transaction_cosmos_message_from_dict = TransactionCosmosMessage.from_dict(transaction_cosmos_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


