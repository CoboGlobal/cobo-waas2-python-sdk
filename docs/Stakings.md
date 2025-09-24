# Stakings

The information about a staking position.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the staking position. | 
**wallet_id** | **str** | The staker&#39;s wallet ID. | 
**address** | **str** | The staker&#39;s wallet address. | 
**amounts** | [**List[AmountDetailsInner]**](AmountDetailsInner.md) | The details about the staking amount. | 
**pool_id** | [**StakingPoolId**](StakingPoolId.md) |  | 
**token_id** | **str** | The token ID. | 
**rewards_info** | **object** | The information about the staking rewards. | [optional] 
**created_timestamp** | **int** | The time when the staking position was created. | 
**updated_timestamp** | **int** | The time when the staking position was last updated. | 
**validator_info** | [**BabylonValidator**](BabylonValidator.md) |  | [optional] 
**validators** | [**List[BabylonValidator]**](BabylonValidator.md) |  | [optional] 
**extra** | [**StakingsExtra**](StakingsExtra.md) |  | [optional] 

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


