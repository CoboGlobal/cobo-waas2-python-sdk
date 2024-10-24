# TriggerTestWebhookEvent201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triggered** | **bool** | Whether a test webhook event was successfully triggered. - &#x60;true&#x60;: The test webhook event was successfully triggered. - &#x60;false&#x60;: The test webhook event could not be triggered.  | [optional] 

## Example

```python
from cobo_waas2.models.trigger_test_webhook_event201_response import TriggerTestWebhookEvent201Response

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerTestWebhookEvent201Response from a JSON string
trigger_test_webhook_event201_response_instance = TriggerTestWebhookEvent201Response.from_json(json)
# print the JSON string representation of the object
print(TriggerTestWebhookEvent201Response.to_json())

# convert the object into a dict
trigger_test_webhook_event201_response_dict = trigger_test_webhook_event201_response_instance.to_dict()
# create an instance of TriggerTestWebhookEvent201Response from a dict
trigger_test_webhook_event201_response_from_dict = TriggerTestWebhookEvent201Response.from_dict(trigger_test_webhook_event201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


