# RevokeApprovalRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_email** | **str** | The email of the user who requested the approval. | 

## Example

```python
from cobo_waas2.models.revoke_approval_request_request import RevokeApprovalRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeApprovalRequestRequest from a JSON string
revoke_approval_request_request_instance = RevokeApprovalRequestRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeApprovalRequestRequest.to_json())

# convert the object into a dict
revoke_approval_request_request_dict = revoke_approval_request_request_instance.to_dict()
# create an instance of RevokeApprovalRequestRequest from a dict
revoke_approval_request_request_from_dict = RevokeApprovalRequestRequest.from_dict(revoke_approval_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


