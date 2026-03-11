# TriggerTestPaymentsWebhookEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**override_data** | **object** | An optional object to customize the webhook event payload. Include only the fields you want to override.  The provided fields must match the webhook event data structure for the specified event type. For the full event data structure, refer to the &#x60;data.data&#x60; property in the response of [List all webhook events](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-all-webhook-events).  If this property is omitted, a default payload is returned.  | [optional] 

## Example

```python
from cobo_waas2.models.trigger_test_payments_webhook_event_request import TriggerTestPaymentsWebhookEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerTestPaymentsWebhookEventRequest from a JSON string
trigger_test_payments_webhook_event_request_instance = TriggerTestPaymentsWebhookEventRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerTestPaymentsWebhookEventRequest.to_json())

# convert the object into a dict
trigger_test_payments_webhook_event_request_dict = trigger_test_payments_webhook_event_request_instance.to_dict()
# create an instance of TriggerTestPaymentsWebhookEventRequest from a dict
trigger_test_payments_webhook_event_request_from_dict = TriggerTestPaymentsWebhookEventRequest.from_dict(trigger_test_payments_webhook_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


