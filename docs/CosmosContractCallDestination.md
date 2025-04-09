# CosmosContractCallDestination

The information about the transaction destination. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**ContractCallDestinationType**](ContractCallDestinationType.md) |  | 
**cosmos_messages** | [**List[CosmosContractCallMessage]**](CosmosContractCallMessage.md) |  | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.cosmos_contract_call_destination import CosmosContractCallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of CosmosContractCallDestination from a JSON string
cosmos_contract_call_destination_instance = CosmosContractCallDestination.from_json(json)
# print the JSON string representation of the object
print(CosmosContractCallDestination.to_json())

# convert the object into a dict
cosmos_contract_call_destination_dict = cosmos_contract_call_destination_instance.to_dict()
# create an instance of CosmosContractCallDestination from a dict
cosmos_contract_call_destination_from_dict = CosmosContractCallDestination.from_dict(cosmos_contract_call_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


