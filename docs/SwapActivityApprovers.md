# SwapActivityApprovers

The approvers data for swap activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The approver name of the swap activity.  | 
**status** | [**SwapApproversStatus**](SwapApproversStatus.md) |  | 

## Example

```python
from cobo_waas2.models.swap_activity_approvers import SwapActivityApprovers

# TODO update the JSON string below
json = "{}"
# create an instance of SwapActivityApprovers from a JSON string
swap_activity_approvers_instance = SwapActivityApprovers.from_json(json)
# print the JSON string representation of the object
print(SwapActivityApprovers.to_json())

# convert the object into a dict
swap_activity_approvers_dict = swap_activity_approvers_instance.to_dict()
# create an instance of SwapActivityApprovers from a dict
swap_activity_approvers_from_dict = SwapActivityApprovers.from_dict(swap_activity_approvers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


