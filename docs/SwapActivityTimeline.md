# SwapActivityTimeline

The timeline of the swap activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action of the swap activity. Possible values include:   - &#x60;Submitted&#x60;: The swap request is submitted.   - &#x60;Pending Authorization&#x60;: The swap request is pending authorization.   - &#x60;Bridge {Token}&#x60;: The token is being bridged to the target chain.   - &#x60;Swap {Token}&#x60;: The token is being swapped on the target chain.   - &#x60;Cobo Confirmation&#x60;: The swap result is waiting for Cobo confirmation.  | 
**status** | **str** | The status of the action. Possible values include:   - &#x60;Success&#x60;: The action is successfully completed.   - &#x60;Processing&#x60;: The action is being processed.   - &#x60;Failed&#x60;: The action has failed.  | 
**timestamp** | **int** | The time when the action took place, in Unix timestamp format, measured in milliseconds.   | [optional] 

## Example

```python
from cobo_waas2.models.swap_activity_timeline import SwapActivityTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of SwapActivityTimeline from a JSON string
swap_activity_timeline_instance = SwapActivityTimeline.from_json(json)
# print the JSON string representation of the object
print(SwapActivityTimeline.to_json())

# convert the object into a dict
swap_activity_timeline_dict = swap_activity_timeline_instance.to_dict()
# create an instance of SwapActivityTimeline from a dict
swap_activity_timeline_from_dict = SwapActivityTimeline.from_dict(swap_activity_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


