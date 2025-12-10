# CreateWebhookEventInfo

The webhook event response model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique event identifier. | 
**channel_id** | **str** | Identifier for the client/organization. Corresponds to organization_id in Cobo Portal. | 
**type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**data** | **str** | JSON serialized object of event data. | 
**wallet_scopes_info** | **Dict[str, object]** | Wallet scope information. | 
**transaction_hash** | **str** | Blockchain transaction hash. | [optional] 
**request_id** | **str** | Request identifier. | [optional] 
**transaction_id** | **str** | Internal transaction identifier. | [optional] 
**cobo_id** | **str** | Cobo internal identifier. | [optional] 
**status** | [**WebhookEventInternalStatus**](WebhookEventInternalStatus.md) |  | 

## Example

```python
from cobo_waas2.models.create_webhook_event_info import CreateWebhookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookEventInfo from a JSON string
create_webhook_event_info_instance = CreateWebhookEventInfo.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookEventInfo.to_json())

# convert the object into a dict
create_webhook_event_info_dict = create_webhook_event_info_instance.to_dict()
# create an instance of CreateWebhookEventInfo from a dict
create_webhook_event_info_from_dict = CreateWebhookEventInfo.from_dict(create_webhook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


