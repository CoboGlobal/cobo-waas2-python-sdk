# RevokeApprovalRequest201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_id** | **str** | The system-generated unique ID of the approval request. | 
**status** | [**ApprovalStatus**](ApprovalStatus.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.revoke_approval_request201_response import RevokeApprovalRequest201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeApprovalRequest201Response from a JSON string
revoke_approval_request201_response_instance = RevokeApprovalRequest201Response.from_json(json)
# print the JSON string representation of the object
print(RevokeApprovalRequest201Response.to_json())

# convert the object into a dict
revoke_approval_request201_response_dict = revoke_approval_request201_response_instance.to_dict()
# create an instance of RevokeApprovalRequest201Response from a dict
revoke_approval_request201_response_from_dict = RevokeApprovalRequest201Response.from_dict(revoke_approval_request201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


