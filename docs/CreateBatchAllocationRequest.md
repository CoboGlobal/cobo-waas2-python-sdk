# CreateBatchAllocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a allocation request. The request ID is provided by you and must be unique. | 
**source_type** | [**PaymentSourceType**](PaymentSourceType.md) |  | 
**allocation_requests** | [**List[AllocationRequest]**](AllocationRequest.md) |  | 

## Example

```python
from cobo_waas2.models.create_batch_allocation_request import CreateBatchAllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchAllocationRequest from a JSON string
create_batch_allocation_request_instance = CreateBatchAllocationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBatchAllocationRequest.to_json())

# convert the object into a dict
create_batch_allocation_request_dict = create_batch_allocation_request_instance.to_dict()
# create an instance of CreateBatchAllocationRequest from a dict
create_batch_allocation_request_from_dict = CreateBatchAllocationRequest.from_dict(create_batch_allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


