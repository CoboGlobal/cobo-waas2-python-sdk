# EvmContractCallDestination

The information about the transaction destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**ContractCallDestinationType**](ContractCallDestinationType.md) |  | 
**address** | **str** | The destination address. | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 
**calldata** | **bytearray** | The data that is used to invoke a specific function or method within the specified contract at the destination address.  | 

## Example

```python
from cobo_waas2.models.evm_contract_call_destination import EvmContractCallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of EvmContractCallDestination from a JSON string
evm_contract_call_destination_instance = EvmContractCallDestination.from_json(json)
# print the JSON string representation of the object
print(EvmContractCallDestination.to_json())

# convert the object into a dict
evm_contract_call_destination_dict = evm_contract_call_destination_instance.to_dict()
# create an instance of EvmContractCallDestination from a dict
evm_contract_call_destination_from_dict = EvmContractCallDestination.from_dict(evm_contract_call_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


