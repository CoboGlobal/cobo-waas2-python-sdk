# TransactionMessageSignEIP191Destination

Information about the transaction destination type `EVM_EIP_191_Signature`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**message** | **str** | The raw data of the message to be signed, encoded in Base64 format. | 

## Example

```python
from cobo_waas2.models.transaction_message_sign_eip191_destination import TransactionMessageSignEIP191Destination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageSignEIP191Destination from a JSON string
transaction_message_sign_eip191_destination_instance = TransactionMessageSignEIP191Destination.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageSignEIP191Destination.to_json())

# convert the object into a dict
transaction_message_sign_eip191_destination_dict = transaction_message_sign_eip191_destination_instance.to_dict()
# create an instance of TransactionMessageSignEIP191Destination from a dict
transaction_message_sign_eip191_destination_from_dict = TransactionMessageSignEIP191Destination.from_dict(transaction_message_sign_eip191_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


