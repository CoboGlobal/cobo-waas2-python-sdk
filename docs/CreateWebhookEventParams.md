# CreateWebhookEventParams

The webhook event payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | Identifier for the client/organization. Corresponds to organization_id in Cobo Portal. | 
**type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**data** | **Dict[str, object]** | The event payload object. | 
**uuid** | **str** | Unique event identifier. | 
**wallet_scopes_info** | **Dict[str, object]** | Wallet scope information. | [optional] 
**transaction_hash** | **str** | Blockchain transaction hash. | [optional] 
**request_id** | **str** | Request identifier. | [optional] 
**transaction_id** | **str** | Internal transaction identifier. | [optional] 
**cobo_id** | **str** | Cobo internal identifier. | [optional] 

## Example

```python
from cobo_waas2.models.create_webhook_event_params import CreateWebhookEventParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookEventParams from a JSON string
create_webhook_event_params_instance = CreateWebhookEventParams.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookEventParams.to_json())

# convert the object into a dict
create_webhook_event_params_dict = create_webhook_event_params_instance.to_dict()
# create an instance of CreateWebhookEventParams from a dict
create_webhook_event_params_from_dict = CreateWebhookEventParams.from_dict(create_webhook_event_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


