# ActivityTimeline

The timeline of the staking activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActivityAction**](ActivityAction.md) |  | 
**status** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**transaction_id** | **str** | The transaction ID. | [optional] 

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


