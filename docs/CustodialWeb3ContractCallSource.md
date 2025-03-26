# CustodialWeb3ContractCallSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**ContractCallSourceType**](ContractCallSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 

## Example

```python
from cobo_waas2.models.custodial_web3_contract_call_source import CustodialWeb3ContractCallSource

# TODO update the JSON string below
json = "{}"
# create an instance of CustodialWeb3ContractCallSource from a JSON string
custodial_web3_contract_call_source_instance = CustodialWeb3ContractCallSource.from_json(json)
# print the JSON string representation of the object
print(CustodialWeb3ContractCallSource.to_json())

# convert the object into a dict
custodial_web3_contract_call_source_dict = custodial_web3_contract_call_source_instance.to_dict()
# create an instance of CustodialWeb3ContractCallSource from a dict
custodial_web3_contract_call_source_from_dict = CustodialWeb3ContractCallSource.from_dict(custodial_web3_contract_call_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


