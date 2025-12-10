# CreateBatchPayoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the batch payout. | 
**token_id** | **str** | The ID of the cryptocurrency used for payout.  | 
**payout_mode** | [**PayoutMode**](PayoutMode.md) |  | 
**unlimited_token_approval** | **bool** | Whether to apply unlimited token allowance. Only applicable when: - &#x60;payout_mode&#x60; is &#x60;SmartContract&#x60;  | [optional] [default to False]
**source** | [**PayoutSource**](PayoutSource.md) |  | 
**destinations** | [**List[PayoutDestination]**](PayoutDestination.md) | The destinations of the payout. | 

## Example

```python
from cobo_waas2.models.create_batch_payout_request import CreateBatchPayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchPayoutRequest from a JSON string
create_batch_payout_request_instance = CreateBatchPayoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBatchPayoutRequest.to_json())

# convert the object into a dict
create_batch_payout_request_dict = create_batch_payout_request_instance.to_dict()
# create an instance of CreateBatchPayoutRequest from a dict
create_batch_payout_request_from_dict = CreateBatchPayoutRequest.from_dict(create_batch_payout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


