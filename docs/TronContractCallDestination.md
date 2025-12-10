# TronContractCallDestination

The information about the transaction destination. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**ContractCallDestinationType**](ContractCallDestinationType.md) |  | 
**address** | **str** | The destination address. | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 TRON, then the value is &#x60;1.5&#x60;.  | [optional] 
**calldata** | **str** | The data that is used to invoke a specific function or method within the specified contract at the destination address.  | 

## Example

```python
from cobo_waas2.models.tron_contract_call_destination import TronContractCallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TronContractCallDestination from a JSON string
tron_contract_call_destination_instance = TronContractCallDestination.from_json(json)
# print the JSON string representation of the object
print(TronContractCallDestination.to_json())

# convert the object into a dict
tron_contract_call_destination_dict = tron_contract_call_destination_instance.to_dict()
# create an instance of TronContractCallDestination from a dict
tron_contract_call_destination_from_dict = TronContractCallDestination.from_dict(tron_contract_call_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


