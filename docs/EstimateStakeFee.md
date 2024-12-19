# EstimateStakeFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ActivityType**](ActivityType.md) |  | 
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. | [optional] 
**source** | [**StakingSource**](StakingSource.md) |  | [optional] 
**pool_id** | [**StakingPoolId**](StakingPoolId.md) |  | 
**amount** | **str** | The amount to stake. | 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 
**extra** | [**CreateStakeActivityExtra**](CreateStakeActivityExtra.md) |  | 

## Example

```python
from cobo_waas2.models.estimate_stake_fee import EstimateStakeFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateStakeFee from a JSON string
estimate_stake_fee_instance = EstimateStakeFee.from_json(json)
# print the JSON string representation of the object
print(EstimateStakeFee.to_json())

# convert the object into a dict
estimate_stake_fee_dict = estimate_stake_fee_instance.to_dict()
# create an instance of EstimateStakeFee from a dict
estimate_stake_fee_from_dict = EstimateStakeFee.from_dict(estimate_stake_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


