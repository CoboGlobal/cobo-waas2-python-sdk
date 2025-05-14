# TSSEvent

The TSS Node event payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The event ID. | [optional] 
**created_timestamp** | **int** | The time when the event occurred, in Unix timestamp format, measured in milliseconds. | [optional] 
**node_id** | **str** | The event publisher&#39;s TSS Node ID. | [optional] 
**event_type** | [**TSSEventType**](TSSEventType.md) |  | 
**data** | [**TSSEventData**](TSSEventData.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_event import TSSEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TSSEvent from a JSON string
tss_event_instance = TSSEvent.from_json(json)
# print the JSON string representation of the object
print(TSSEvent.to_json())

# convert the object into a dict
tss_event_dict = tss_event_instance.to_dict()
# create an instance of TSSEvent from a dict
tss_event_from_dict = TSSEvent.from_dict(tss_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


