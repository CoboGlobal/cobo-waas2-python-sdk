# UpdateWebhookEndpointByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribed_events** | [**List[WebhookEventType]**](WebhookEventType.md) | The new event types you want to subscribe to for this webhook endpoint. You can call [Get webhook event types](https://www.cobo.com/developers/v2/api-references/developers--webhooks/get-webhook-event-types) to retrieve all available event types. | [optional] 
**status** | **str** | The new status you want to set the webhook endpoint to. If you set &#x60;status&#x60; to &#x60;STATUS_INACTIVE&#x60;, the endpoint will be revoked, meaning it will no longer receive any webhook events. | [optional] 
**description** | **str** | The webhook endpoint description. | [optional] 

## Example

```python
from cobo_waas2.models.update_webhook_endpoint_by_id_request import UpdateWebhookEndpointByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookEndpointByIdRequest from a JSON string
update_webhook_endpoint_by_id_request_instance = UpdateWebhookEndpointByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookEndpointByIdRequest.to_json())

# convert the object into a dict
update_webhook_endpoint_by_id_request_dict = update_webhook_endpoint_by_id_request_instance.to_dict()
# create an instance of UpdateWebhookEndpointByIdRequest from a dict
update_webhook_endpoint_by_id_request_from_dict = UpdateWebhookEndpointByIdRequest.from_dict(update_webhook_endpoint_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


