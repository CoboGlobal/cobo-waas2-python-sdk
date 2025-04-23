# CosmosAdr36MessageSignDestination

The information about the destination `COSMOS_ADR_36_Signature`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**MessageSignDestinationType**](MessageSignDestinationType.md) |  | 
**message_cosmos_adr36** | **str** | Message to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.cosmos_adr36_message_sign_destination import CosmosAdr36MessageSignDestination

# TODO update the JSON string below
json = "{}"
# create an instance of CosmosAdr36MessageSignDestination from a JSON string
cosmos_adr36_message_sign_destination_instance = CosmosAdr36MessageSignDestination.from_json(json)
# print the JSON string representation of the object
print(CosmosAdr36MessageSignDestination.to_json())

# convert the object into a dict
cosmos_adr36_message_sign_destination_dict = cosmos_adr36_message_sign_destination_instance.to_dict()
# create an instance of CosmosAdr36MessageSignDestination from a dict
cosmos_adr36_message_sign_destination_from_dict = CosmosAdr36MessageSignDestination.from_dict(cosmos_adr36_message_sign_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


