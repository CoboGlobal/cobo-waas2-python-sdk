# EstimateWithdrawFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ActivityType**](ActivityType.md) |  | 
**staking_id** | **str** | The id of the related staking. | 
**amount** | **str** | The amount to stake | [optional] 
**address** | **str** | The withdraw to address. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 

## Example

```python
from cobo_waas2.models.estimate_withdraw_fee import EstimateWithdrawFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateWithdrawFee from a JSON string
estimate_withdraw_fee_instance = EstimateWithdrawFee.from_json(json)
# print the JSON string representation of the object
print(EstimateWithdrawFee.to_json())

# convert the object into a dict
estimate_withdraw_fee_dict = estimate_withdraw_fee_instance.to_dict()
# create an instance of EstimateWithdrawFee from a dict
estimate_withdraw_fee_from_dict = EstimateWithdrawFee.from_dict(estimate_withdraw_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


