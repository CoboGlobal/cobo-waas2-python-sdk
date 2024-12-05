# EstimateClaimFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ActivityType**](ActivityType.md) |  | 
**staking_id** | **str** | The staking ID of the staking. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimate_claim_fee import EstimateClaimFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateClaimFee from a JSON string
estimate_claim_fee_instance = EstimateClaimFee.from_json(json)
# print the JSON string representation of the object
print(EstimateClaimFee.to_json())

# convert the object into a dict
estimate_claim_fee_dict = estimate_claim_fee_instance.to_dict()
# create an instance of EstimateClaimFee from a dict
estimate_claim_fee_from_dict = EstimateClaimFee.from_dict(estimate_claim_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


