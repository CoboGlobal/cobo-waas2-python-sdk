# EvmEIP191MessageSignDestination

The information about the destination `EVM_EIP_191_Signature`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**message** | **str** | The raw data of the message to be signed, encoded in Base64 format. | 

## Example

```python
from cobo_waas2.models.evm_eip191_message_sign_destination import EvmEIP191MessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of EvmEIP191MessageSignDestination from a JSON string
evm_eip191_message_sign_destination_instance = EvmEIP191MessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(EvmEIP191MessageSignDestination.to_json())

# convert the object into a dict
evm_eip191_message_sign_destination_dict = evm_eip191_message_sign_destination_instance.to_dict()
# create an instance of EvmEIP191MessageSignDestination from a dict
evm_eip191_message_sign_destination_from_dict = EvmEIP191MessageSignDestination.from_dict(evm_eip191_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


