# WebhookEventDataType

The data type of the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. | 

## Example

```python
from cobo_waas2.models.webhook_event_data_type import WebhookEventDataType

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventDataType from a JSON string
webhook_event_data_type_instance = WebhookEventDataType.from_json(json)
# print the JSON string representation of the object
print(WebhookEventDataType.to_json())

# convert the object into a dict
webhook_event_data_type_dict = webhook_event_data_type_instance.to_dict()
# create an instance of WebhookEventDataType from a dict
webhook_event_data_type_from_dict = WebhookEventDataType.from_dict(webhook_event_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


