# WebhookEventLog

The webhook event log.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The event log ID. | 
**created_timestamp** | **int** | The time when the log was created, in Unix timestamp format, measured in milliseconds. | 
**request_headers** | **object** | The request headers of the webhook event. | 
**request_body** | [**WebhookEvent**](WebhookEvent.md) |  | 
**response_body** | **str** | The response body of the webhook event. | [optional] 
**response_status_code** | **int** | The response status code of the webhook event. | [optional] 
**response_time** | **int** | The response time of the webhook event, in milliseconds. | [optional] 
**success** | **bool** | Whether the webhook event has been successfully delivered. | 
**failure_reason** | **str** | The reason why the webhook event fails to be delivered. | [optional] 

## Example

```python
from cobo_waas2.models.webhook_event_log import WebhookEventLog

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventLog from a JSON string
webhook_event_log_instance = WebhookEventLog.from_json(json)
# print the JSON string representation of the object
print(WebhookEventLog.to_json())

# convert the object into a dict
webhook_event_log_dict = webhook_event_log_instance.to_dict()
# create an instance of WebhookEventLog from a dict
webhook_event_log_from_dict = WebhookEventLog.from_dict(webhook_event_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


