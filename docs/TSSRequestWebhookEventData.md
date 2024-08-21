# TSSRequestWebhookEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. | 
**tss_request_id** | **str** | The TSS request ID. | [optional] 
**source_key_share_holder_group** | [**SourceGroup**](SourceGroup.md) |  | [optional] 
**target_key_share_holder_group_id** | **str** | The target key share holder group ID. | [optional] 
**type** | [**TSSRequestType**](TSSRequestType.md) |  | [optional] 
**status** | [**TSSRequestStatus**](TSSRequestStatus.md) |  | [optional] 
**description** | **str** | The description of the TSS request. | [optional] 
**created_timestamp** | **int** | The TSS request&#39;s creation time in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.tss_request_webhook_event_data import TSSRequestWebhookEventData

# TODO update the JSON string below
json = "{}"
# create an instance of TSSRequestWebhookEventData from a JSON string
tss_request_webhook_event_data_instance = TSSRequestWebhookEventData.from_json(json)
# print the JSON string representation of the object
print(TSSRequestWebhookEventData.to_json())

# convert the object into a dict
tss_request_webhook_event_data_dict = tss_request_webhook_event_data_instance.to_dict()
# create an instance of TSSRequestWebhookEventData from a dict
tss_request_webhook_event_data_from_dict = TSSRequestWebhookEventData.from_dict(tss_request_webhook_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


