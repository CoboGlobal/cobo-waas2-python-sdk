# ListWebhookEventDefinitions200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**WebhookEventType**](WebhookEventType.md) |  | [optional] 
**description** | **str** | The description of the webhook event type. | [optional] 

## Example

```python
from cobo_waas2.models.list_webhook_event_definitions200_response_inner import ListWebhookEventDefinitions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookEventDefinitions200ResponseInner from a JSON string
list_webhook_event_definitions200_response_inner_instance = ListWebhookEventDefinitions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListWebhookEventDefinitions200ResponseInner.to_json())

# convert the object into a dict
list_webhook_event_definitions200_response_inner_dict = list_webhook_event_definitions200_response_inner_instance.to_dict()
# create an instance of ListWebhookEventDefinitions200ResponseInner from a dict
list_webhook_event_definitions200_response_inner_from_dict = ListWebhookEventDefinitions200ResponseInner.from_dict(list_webhook_event_definitions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


