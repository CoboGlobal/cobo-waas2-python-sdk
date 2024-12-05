# GetStakingEstimationFeeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ActivityType**](ActivityType.md) |  | 
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. | [optional] 
**source** | [**StakingSource**](StakingSource.md) |  | [optional] 
**pool_id** | [**StakingPoolId**](StakingPoolId.md) |  | 
**amount** | **str** | The amount to withdraw. | 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 
**extra** | [**CreateUnstakeActivityExtra**](CreateUnstakeActivityExtra.md) |  | 
**staking_id** | **str** | The staking ID of the staking. | 

## Example

```python
from cobo_waas2.models.get_staking_estimation_fee_request import GetStakingEstimationFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStakingEstimationFeeRequest from a JSON string
get_staking_estimation_fee_request_instance = GetStakingEstimationFeeRequest.from_json(json)
# print the JSON string representation of the object
print(GetStakingEstimationFeeRequest.to_json())

# convert the object into a dict
get_staking_estimation_fee_request_dict = get_staking_estimation_fee_request_instance.to_dict()
# create an instance of GetStakingEstimationFeeRequest from a dict
get_staking_estimation_fee_request_from_dict = GetStakingEstimationFeeRequest.from_dict(get_staking_estimation_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


