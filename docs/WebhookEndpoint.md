# WebhookEndpoint

The information about a webhook endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The webhook endpoint URL. | 
**subscribed_events** | [**List[WebhookEventType]**](WebhookEventType.md) | The event types subscribed by a webhook endpoint. | 
**created_timestamp** | **int** | The time when the endpoint was registered, in Unix timestamp format, measured in seconds. | 
**endpoint_id** | **str** | The webhook endpoint ID. | [optional] 
**status** | [**WebhookEndpointStatus**](WebhookEndpointStatus.md) |  | 
**description** | **str** | The description of the webhook endpoint. | [optional] 

## Example

```python
from cobo_waas2.models.webhook_endpoint import WebhookEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEndpoint from a JSON string
webhook_endpoint_instance = WebhookEndpoint.from_json(json)
# print the JSON string representation of the object
print(WebhookEndpoint.to_json())

# convert the object into a dict
webhook_endpoint_dict = webhook_endpoint_instance.to_dict()
# create an instance of WebhookEndpoint from a dict
webhook_endpoint_from_dict = WebhookEndpoint.from_dict(webhook_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


