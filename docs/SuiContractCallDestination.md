# SuiContractCallDestination

The information about the transaction destination. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**ContractCallDestinationType**](ContractCallDestinationType.md) |  | 
**contract_param** | [**SuiContractCallContractParam**](SuiContractCallContractParam.md) |  | 

## Example

```python
from cobo_waas2.models.sui_contract_call_destination import SuiContractCallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of SuiContractCallDestination from a JSON string
sui_contract_call_destination_instance = SuiContractCallDestination.from_json(json)
# print the JSON string representation of the object
print(SuiContractCallDestination.to_json())

# convert the object into a dict
sui_contract_call_destination_dict = sui_contract_call_destination_instance.to_dict()
# create an instance of SuiContractCallDestination from a dict
sui_contract_call_destination_from_dict = SuiContractCallDestination.from_dict(sui_contract_call_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


