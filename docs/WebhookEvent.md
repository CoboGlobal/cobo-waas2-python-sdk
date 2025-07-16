# WebhookEvent

The webhook event payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The event ID. | [optional] 
**url** | **str** | The webhook endpoint URL. | 
**created_timestamp** | **int** | The time when the event was triggered, in Unix timestamp format (milliseconds). - The value remains unchanged across retries. - The default webhook timeout is 2 seconds.  | 
**type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**data** | [**WebhookEventData**](WebhookEventData.md) |  | 
**status** | [**WebhookEventStatus**](WebhookEventStatus.md) |  | [optional] 
**next_retry_timestamp** | **int** | The timestamp indicating the next scheduled retry to deliver this event, in Unix timestamp format, measured in milliseconds. This field is only present if the event status is &#x60;Retrying&#x60;.  | [optional] 
**retries_left** | **int** | The number of retries left. This field is only present if the event status is &#x60;Retrying&#x60;. | [optional] 

## Example

```python
from cobo_waas2.models.webhook_event import WebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEvent from a JSON string
webhook_event_instance = WebhookEvent.from_json(json)
# print the JSON string representation of the object
print(WebhookEvent.to_json())

# convert the object into a dict
webhook_event_dict = webhook_event_instance.to_dict()
# create an instance of WebhookEvent from a dict
webhook_event_from_dict = WebhookEvent.from_dict(webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


