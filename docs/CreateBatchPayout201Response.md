# CreateBatchPayout201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** | The payout ID. | 
**payout_mode** | [**PayoutMode**](PayoutMode.md) |  | 
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**estimated_total_fee** | **str** | The total fee of the payout. | 
**created_timestamp** | **int** | The created time of the payout, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.create_batch_payout201_response import CreateBatchPayout201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchPayout201Response from a JSON string
create_batch_payout201_response_instance = CreateBatchPayout201Response.from_json(json)
# print the JSON string representation of the object
print(CreateBatchPayout201Response.to_json())

# convert the object into a dict
create_batch_payout201_response_dict = create_batch_payout201_response_instance.to_dict()
# create an instance of CreateBatchPayout201Response from a dict
create_batch_payout201_response_from_dict = CreateBatchPayout201Response.from_dict(create_batch_payout201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


