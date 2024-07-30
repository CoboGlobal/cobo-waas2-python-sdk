# StakingSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**ContractCallSourceType**](ContractCallSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 
**nonce** | **int** | The transaction nonce. | [optional] 
**delegate** | [**CoboSafeDelegate**](CoboSafeDelegate.md) |  | 

## Example

```python
from cobo_waas2.models.staking_source import StakingSource

# TODO update the JSON string below
json = "{}"
# create an instance of StakingSource from a JSON string
staking_source_instance = StakingSource.from_json(json)
# print the JSON string representation of the object
print(StakingSource.to_json())

# convert the object into a dict
staking_source_dict = staking_source_instance.to_dict()
# create an instance of StakingSource from a dict
staking_source_from_dict = StakingSource.from_dict(staking_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


