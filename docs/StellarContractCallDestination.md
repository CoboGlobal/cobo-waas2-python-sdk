# StellarContractCallDestination

The information about the transaction destination. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**ContractCallDestinationType**](ContractCallDestinationType.md) |  | 
**contract_param** | [**StellarContractCallContractParam**](StellarContractCallContractParam.md) |  | 

## Example

```python
from cobo_waas2.models.stellar_contract_call_destination import StellarContractCallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of StellarContractCallDestination from a JSON string
stellar_contract_call_destination_instance = StellarContractCallDestination.from_json(json)
# print the JSON string representation of the object
print(StellarContractCallDestination.to_json())

# convert the object into a dict
stellar_contract_call_destination_dict = stellar_contract_call_destination_instance.to_dict()
# create an instance of StellarContractCallDestination from a dict
stellar_contract_call_destination_from_dict = StellarContractCallDestination.from_dict(stellar_contract_call_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


