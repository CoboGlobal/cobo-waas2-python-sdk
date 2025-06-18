# ApprovalRequest

The information of an approval request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_id** | **str** | The system-generated unique ID of the approval request. | 
**request_id** | **str** | An identifier provided by you when requesting the approval. | 
**fields** | [**List[AppWorkflowField]**](AppWorkflowField.md) |  | 
**status** | [**ApprovalStatus**](ApprovalStatus.md) |  | 
**initiated_timestamp** | **int** | The time when the approval was initiated, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.approval_request import ApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequest from a JSON string
approval_request_instance = ApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequest.to_json())

# convert the object into a dict
approval_request_dict = approval_request_instance.to_dict()
# create an instance of ApprovalRequest from a dict
approval_request_from_dict = ApprovalRequest.from_dict(approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


