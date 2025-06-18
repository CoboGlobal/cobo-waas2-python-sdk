# RequestApproval

The information about a approval request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** | The unique ID of the approval workflow. | 
**request_id** | **str** | An identifier provided by you to track this request. | 
**initiator_email** | **str** | The email of the user who requested the approval. | 
**fields** | [**List[AppWorkflowField]**](AppWorkflowField.md) |  | 
**guard_template** | **str** | The template of a Cobo Guard message. Please connect [help@cobo.com](mailto:help@cobo.com) to get the template content. | 

## Example

```python
from cobo_waas2.models.request_approval import RequestApproval

# TODO update the JSON string below
json = "{}"
# create an instance of RequestApproval from a JSON string
request_approval_instance = RequestApproval.from_json(json)
# print the JSON string representation of the object
print(RequestApproval.to_json())

# convert the object into a dict
request_approval_dict = request_approval_instance.to_dict()
# create an instance of RequestApproval from a dict
request_approval_from_dict = RequestApproval.from_dict(request_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


