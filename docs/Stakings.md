# Stakings

The staking info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the stake. | 
**wallet_id** | **str** | The unique wallet id. | 
**address** | **str** | The staker wallet address. | 
**amounts** | [**List[AmountDetailsInner]**](AmountDetailsInner.md) | The staking amount details. | 
**initiator** | **str** | The initiator of the stake. | [optional] 
**unlock_timestamp** | **int** | The unlock time. | [optional] 
**unlock_block_height** | **int** | The unlock block height. | [optional] 
**pool_id** | **str** | The unique pool id. | 
**token_id** | **str** | The token id. | 
**pos_chain** | **str** | The pos chain of the stake. | [optional] 
**rewards_info** | **object** | The rewards info of the stake. | [optional] 
**created_timestamp** | **int** | The time when the stake was created. | 
**updated_timestamp** | **int** | The time when the stake was last updated. | 
**validator_info** | [**StakingsValidatorInfo**](StakingsValidatorInfo.md) |  | 

## Example

```python
from cobo_waas2.models.stakings import Stakings

# TODO update the JSON string below
json = "{}"
# create an instance of Stakings from a JSON string
stakings_instance = Stakings.from_json(json)
# print the JSON string representation of the object
print(Stakings.to_json())

# convert the object into a dict
stakings_dict = stakings_instance.to_dict()
# create an instance of Stakings from a dict
stakings_from_dict = Stakings.from_dict(stakings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


