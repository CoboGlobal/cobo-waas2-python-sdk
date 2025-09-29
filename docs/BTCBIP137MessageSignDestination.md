# BTCBIP137MessageSignDestination

The information about the destination `BTC_BIP_137`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**message_bip137** | **str** | Message to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.btcbip137_message_sign_destination import BTCBIP137MessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of BTCBIP137MessageSignDestination from a JSON string
btcbip137_message_sign_destination_instance = BTCBIP137MessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(BTCBIP137MessageSignDestination.to_json())

# convert the object into a dict
btcbip137_message_sign_destination_dict = btcbip137_message_sign_destination_instance.to_dict()
# create an instance of BTCBIP137MessageSignDestination from a dict
btcbip137_message_sign_destination_from_dict = BTCBIP137MessageSignDestination.from_dict(btcbip137_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


