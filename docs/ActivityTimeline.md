# ActivityTimeline

The timeline of the staking activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActivityAction**](ActivityAction.md) |  | 
**status** | **str** | The status of the action. Possible values include:   - &#x60;Success&#x60;: The action is successfully completed.   - &#x60;Processing&#x60;: The action is being processed.   - &#x60;Failed&#x60;: The action has failed.  | [optional] 
**timestamp** | **int** | The time when the action took place, in Unix timestamp format, measured in milliseconds.  - For the &#x60;Submitted&#x60; action, &#x60;timestamp&#x60; represents the time the staking, unstaking, or withdrawal request was created.  - For the &#x60;BTCConfirmation&#x60; action, &#x60;timestamp&#x60; represents the time when the request was confirmed on the Bitcoin chain, or when the confirmation failed. - For the &#x60;BabylonConfirmation&#x60; action, &#x60;timestamp&#x60; represents the time when the request was confirmed by the Babylon protocol, or when the confirmation failed.  | [optional] 
**transaction_id** | **str** | The ID of the corresponding transaction. | [optional] 

## Example

```python
from cobo_waas2.models.activity_timeline import ActivityTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTimeline from a JSON string
activity_timeline_instance = ActivityTimeline.from_json(json)
# print the JSON string representation of the object
print(ActivityTimeline.to_json())

# convert the object into a dict
activity_timeline_dict = activity_timeline_instance.to_dict()
# create an instance of ActivityTimeline from a dict
activity_timeline_from_dict = ActivityTimeline.from_dict(activity_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


