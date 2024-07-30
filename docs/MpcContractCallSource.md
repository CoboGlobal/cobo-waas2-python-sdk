# MpcContractCallSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**ContractCallSourceType**](ContractCallSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 
**nonce** | **int** | The transaction nonce. | [optional] 

## Example

```python
from cobo_waas2.models.mpc_contract_call_source import MpcContractCallSource

# TODO update the JSON string below
json = "{}"
# create an instance of MpcContractCallSource from a JSON string
mpc_contract_call_source_instance = MpcContractCallSource.from_json(json)
# print the JSON string representation of the object
print(MpcContractCallSource.to_json())

# convert the object into a dict
mpc_contract_call_source_dict = mpc_contract_call_source_instance.to_dict()
# create an instance of MpcContractCallSource from a dict
mpc_contract_call_source_from_dict = MpcContractCallSource.from_dict(mpc_contract_call_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


