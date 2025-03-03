# BTCEIP191MessageSignDestination

The information about the destination `BTC_EIP_191_Signature`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**message** | **str** | The raw data of the message to be signed, encoded in Base64 format. | 

## Example

```python
from cobo_waas2.models.btceip191_message_sign_destination import BTCEIP191MessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of BTCEIP191MessageSignDestination from a JSON string
btceip191_message_sign_destination_instance = BTCEIP191MessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(BTCEIP191MessageSignDestination.to_json())

# convert the object into a dict
btceip191_message_sign_destination_dict = btceip191_message_sign_destination_instance.to_dict()
# create an instance of BTCEIP191MessageSignDestination from a dict
btceip191_message_sign_destination_from_dict = BTCEIP191MessageSignDestination.from_dict(btceip191_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


