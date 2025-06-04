# BTCBIP322MessageSignDestination

The information about the destination `BTC_BIP_322`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**message_bip322** | **str** | Message to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.btcbip322_message_sign_destination import BTCBIP322MessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of BTCBIP322MessageSignDestination from a JSON string
btcbip322_message_sign_destination_instance = BTCBIP322MessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(BTCBIP322MessageSignDestination.to_json())

# convert the object into a dict
btcbip322_message_sign_destination_dict = btcbip322_message_sign_destination_instance.to_dict()
# create an instance of BTCBIP322MessageSignDestination from a dict
btcbip322_message_sign_destination_from_dict = BTCBIP322MessageSignDestination.from_dict(btcbip322_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


