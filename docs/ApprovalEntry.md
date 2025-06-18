# ApprovalEntry

The information of an approval request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ApprovalStatus**](ApprovalStatus.md) |  | 
**created_timestamp** | **int** | The time when the approval was created, in Unix timestamp format, measured in milliseconds. | 
**approval_users** | [**List[ApprovalUser]**](ApprovalUser.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.approval_entry import ApprovalEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalEntry from a JSON string
approval_entry_instance = ApprovalEntry.from_json(json)
# print the JSON string representation of the object
print(ApprovalEntry.to_json())

# convert the object into a dict
approval_entry_dict = approval_entry_instance.to_dict()
# create an instance of ApprovalEntry from a dict
approval_entry_from_dict = ApprovalEntry.from_dict(approval_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


