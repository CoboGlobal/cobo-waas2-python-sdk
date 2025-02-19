# MessageSignDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**message** | **str** | The raw data of the message to be signed, encoded in Base64 format. | 
**structured_data** | **Dict[str, object]** | The structured data to be signed, formatted as a JSON object according to the EIP-712 standard. | 
**msg_hash** | **str** | Message hash to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.message_sign_destination import MessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSignDestination from a JSON string
message_sign_destination_instance = MessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(MessageSignDestination.to_json())

# convert the object into a dict
message_sign_destination_dict = message_sign_destination_instance.to_dict()
# create an instance of MessageSignDestination from a dict
message_sign_destination_from_dict = MessageSignDestination.from_dict(message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


