# TriggerTestWebhookEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**override_data** | **object** | An object for customization of the webhook event payload. You only need to include the fields you want to customize.   The provided fields must match the webhook event data structure, depending on the specified event type. For a complete introduction of the webhook event data structure, refer to the &#x60;data.data&#x60; property in the response of [List all webhook events](/v2/api-references/developers--webhooks/list-all-webhook-events).  If this property is not provided, a default payload will be returned.  | [optional] 

## Example

```python
from cobo_waas2.models.trigger_test_webhook_event_request import TriggerTestWebhookEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerTestWebhookEventRequest from a JSON string
trigger_test_webhook_event_request_instance = TriggerTestWebhookEventRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerTestWebhookEventRequest.to_json())

# convert the object into a dict
trigger_test_webhook_event_request_dict = trigger_test_webhook_event_request_instance.to_dict()
# create an instance of TriggerTestWebhookEventRequest from a dict
trigger_test_webhook_event_request_from_dict = TriggerTestWebhookEventRequest.from_dict(trigger_test_webhook_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


