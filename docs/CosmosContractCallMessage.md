# CosmosContractCallMessage

The information about the Cosmos message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_url** | **str** | The type URL of the Cosmos message.  | 
**message** | **str** | The Base64-encoded Cosmos message.  | 

## Example

```python
from cobo_waas2.models.cosmos_contract_call_message import CosmosContractCallMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CosmosContractCallMessage from a JSON string
cosmos_contract_call_message_instance = CosmosContractCallMessage.from_json(json)
# print the JSON string representation of the object
print(CosmosContractCallMessage.to_json())

# convert the object into a dict
cosmos_contract_call_message_dict = cosmos_contract_call_message_instance.to_dict()
# create an instance of CosmosContractCallMessage from a dict
cosmos_contract_call_message_from_dict = CosmosContractCallMessage.from_dict(cosmos_contract_call_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


