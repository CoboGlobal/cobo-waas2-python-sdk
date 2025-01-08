# BaseContractCallSource

The information about the transaction source type `Org-Controlled` and `User-Controlled`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**ContractCallSourceType**](ContractCallSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 

## Example

```python
from cobo_waas2.models.base_contract_call_source import BaseContractCallSource

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContractCallSource from a JSON string
base_contract_call_source_instance = BaseContractCallSource.from_json(json)
# print the JSON string representation of the object
print(BaseContractCallSource.to_json())

# convert the object into a dict
base_contract_call_source_dict = base_contract_call_source_instance.to_dict()
# create an instance of BaseContractCallSource from a dict
base_contract_call_source_from_dict = BaseContractCallSource.from_dict(base_contract_call_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


