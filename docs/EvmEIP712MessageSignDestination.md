# EvmEIP712MessageSignDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**structured_data** | **Dict[str, object]** | The structured data to be signed, formatted as a JSON object according to the EIP-712 standard. | 

## Example

```python
from cobo_waas2.models.evm_eip712_message_sign_destination import EvmEIP712MessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of EvmEIP712MessageSignDestination from a JSON string
evm_eip712_message_sign_destination_instance = EvmEIP712MessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(EvmEIP712MessageSignDestination.to_json())

# convert the object into a dict
evm_eip712_message_sign_destination_dict = evm_eip712_message_sign_destination_instance.to_dict()
# create an instance of EvmEIP712MessageSignDestination from a dict
evm_eip712_message_sign_destination_from_dict = EvmEIP712MessageSignDestination.from_dict(evm_eip712_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


