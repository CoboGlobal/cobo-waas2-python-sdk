# ReceivedAmountPerAddress

The total amount of the token that has been received at a given address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The receiving address. | 
**total_received_amount** | **str** | The total amount of the token that has been received at this address. | 

## Example

```python
from cobo_waas2.models.received_amount_per_address import ReceivedAmountPerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedAmountPerAddress from a JSON string
received_amount_per_address_instance = ReceivedAmountPerAddress.from_json(json)
# print the JSON string representation of the object
print(ReceivedAmountPerAddress.to_json())

# convert the object into a dict
received_amount_per_address_dict = received_amount_per_address_instance.to_dict()
# create an instance of ReceivedAmountPerAddress from a dict
received_amount_per_address_from_dict = ReceivedAmountPerAddress.from_dict(received_amount_per_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


