# TransactionMessageSignEIP712Destination

Information about the transaction destination type `EVM_EIP_712_Signature`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**structured_data** | **Dict[str, object]** | The structured data to be signed, formatted as a JSON object according to the EIP-712 standard. | 

## Example

```python
from cobo_waas2.models.transaction_message_sign_eip712_destination import TransactionMessageSignEIP712Destination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageSignEIP712Destination from a JSON string
transaction_message_sign_eip712_destination_instance = TransactionMessageSignEIP712Destination.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageSignEIP712Destination.to_json())

# convert the object into a dict
transaction_message_sign_eip712_destination_dict = transaction_message_sign_eip712_destination_instance.to_dict()
# create an instance of TransactionMessageSignEIP712Destination from a dict
transaction_message_sign_eip712_destination_from_dict = TransactionMessageSignEIP712Destination.from_dict(transaction_message_sign_eip712_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


