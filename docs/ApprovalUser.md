# ApprovalUser

The information of an app workflow approval user entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The approval user email. | 
**name** | **str** | The approval user name. | [optional] 
**status** | [**ApprovalStatus**](ApprovalStatus.md) |  | 
**created_timestamp** | **int** | The time when the approval was created, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.approval_user import ApprovalUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalUser from a JSON string
approval_user_instance = ApprovalUser.from_json(json)
# print the JSON string representation of the object
print(ApprovalUser.to_json())

# convert the object into a dict
approval_user_dict = approval_user_instance.to_dict()
# create an instance of ApprovalUser from a dict
approval_user_from_dict = ApprovalUser.from_dict(approval_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


