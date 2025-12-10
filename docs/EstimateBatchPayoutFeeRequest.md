# EstimateBatchPayoutFeeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency used for payout.  | 
**payout_mode** | [**PayoutMode**](PayoutMode.md) |  | 
**source** | [**PayoutSource**](PayoutSource.md) |  | 
**destinations** | [**List[PayoutDestination]**](PayoutDestination.md) | The destinations of the payout. | 
**rbf_type** | [**PayoutRbfType**](PayoutRbfType.md) |  | [optional] 
**replaced_payout_id** | **str** | The ID of the payout that this payout replaced. | [optional] 

## Example

```python
from cobo_waas2.models.estimate_batch_payout_fee_request import EstimateBatchPayoutFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateBatchPayoutFeeRequest from a JSON string
estimate_batch_payout_fee_request_instance = EstimateBatchPayoutFeeRequest.from_json(json)
# print the JSON string representation of the object
print(EstimateBatchPayoutFeeRequest.to_json())

# convert the object into a dict
estimate_batch_payout_fee_request_dict = estimate_batch_payout_fee_request_instance.to_dict()
# create an instance of EstimateBatchPayoutFeeRequest from a dict
estimate_batch_payout_fee_request_from_dict = EstimateBatchPayoutFeeRequest.from_dict(estimate_batch_payout_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


