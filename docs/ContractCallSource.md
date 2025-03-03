# ContractCallSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**ContractCallSourceType**](ContractCallSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 
**mpc_used_key_share_holder_group** | [**MpcSigningGroup**](MpcSigningGroup.md) |  | [optional] 
**delegate** | [**CoboSafeDelegate**](CoboSafeDelegate.md) |  | 

## Example

```python
from cobo_waas2.models.contract_call_source import ContractCallSource

# TODO update the JSON string below
json = "{}"
# create an instance of ContractCallSource from a JSON string
contract_call_source_instance = ContractCallSource.from_json(json)
# print the JSON string representation of the object
print(ContractCallSource.to_json())

# convert the object into a dict
contract_call_source_dict = contract_call_source_instance.to_dict()
# create an instance of ContractCallSource from a dict
contract_call_source_from_dict = ContractCallSource.from_dict(contract_call_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


