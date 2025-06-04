# TransactionMessageSignBTCEIP191Destination

The information about the destination `BTC_EIP_191_Signature`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**message** | **str** | The raw data of the message to be signed, encoded in Base64 format. | 

## Example

```python
from cobo_waas2.models.transaction_message_sign_btceip191_destination import TransactionMessageSignBTCEIP191Destination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageSignBTCEIP191Destination from a JSON string
transaction_message_sign_btceip191_destination_instance = TransactionMessageSignBTCEIP191Destination.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageSignBTCEIP191Destination.to_json())

# convert the object into a dict
transaction_message_sign_btceip191_destination_dict = transaction_message_sign_btceip191_destination_instance.to_dict()
# create an instance of TransactionMessageSignBTCEIP191Destination from a dict
transaction_message_sign_btceip191_destination_from_dict = TransactionMessageSignBTCEIP191Destination.from_dict(transaction_message_sign_btceip191_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


