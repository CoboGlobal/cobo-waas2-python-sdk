# ContractCallDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**ContractCallDestinationType**](ContractCallDestinationType.md) |  | 
**address** | **str** | The destination address. | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 
**calldata** | **str** | The data used to invoke a specific function or method within the specified contract at the destination address, with a maximum length of 65,000 characters.  | 
**instructions** | [**List[SolContractCallInstruction]**](SolContractCallInstruction.md) |  | 

## Example

```python
from cobo_waas2.models.contract_call_destination import ContractCallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ContractCallDestination from a JSON string
contract_call_destination_instance = ContractCallDestination.from_json(json)
# print the JSON string representation of the object
print(ContractCallDestination.to_json())

# convert the object into a dict
contract_call_destination_dict = contract_call_destination_instance.to_dict()
# create an instance of ContractCallDestination from a dict
contract_call_destination_from_dict = ContractCallDestination.from_dict(contract_call_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


