# RawMessageSignDestination

The information about the destination `Raw_Message_Signature`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**msg_hash** | **str** | Message hash to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.raw_message_sign_destination import RawMessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of RawMessageSignDestination from a JSON string
raw_message_sign_destination_instance = RawMessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(RawMessageSignDestination.to_json())

# convert the object into a dict
raw_message_sign_destination_dict = raw_message_sign_destination_instance.to_dict()
# create an instance of RawMessageSignDestination from a dict
raw_message_sign_destination_from_dict = RawMessageSignDestination.from_dict(raw_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


