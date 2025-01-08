# CreateWebhookEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The webhook endpoint URL. | 
**subscribed_events** | [**List[WebhookEventType]**](WebhookEventType.md) | The event types you want to subscribe to for this webhook endpoint. You can call [Get webhook event types](https://www.cobo.com/developers/v2/api-references/developers--webhooks/get-webhook-event-types) to retrieve all available event types.  | 
**description** | **str** | The description of the webhook endpoint. | [optional] 

## Example

```python
from cobo_waas2.models.create_webhook_endpoint_request import CreateWebhookEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookEndpointRequest from a JSON string
create_webhook_endpoint_request_instance = CreateWebhookEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookEndpointRequest.to_json())

# convert the object into a dict
create_webhook_endpoint_request_dict = create_webhook_endpoint_request_instance.to_dict()
# create an instance of CreateWebhookEndpointRequest from a dict
create_webhook_endpoint_request_from_dict = CreateWebhookEndpointRequest.from_dict(create_webhook_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


