# CallbackMessage

The information about a callback message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The callback message ID. | 
**created_timestamp** | **int** | The time when the callback message was created, in Unix timestamp format, measured in milliseconds. | 
**updated_timestamp** | **int** | The time when the callback message was updated, in Unix timestamp format, measured in milliseconds. | 
**request_id** | **str** | The request ID of the transaction. | 
**transaction_id** | **str** | The transaction ID. | 
**wallet_id** | **str** | The wallet ID. | [optional] 
**url** | **str** | The callback endpoint URL. | 
**data** | [**Transaction**](Transaction.md) |  | 
**status** | **str** | The callback message status. Possible values include &#x60;Denied&#x60;, &#x60;Approved&#x60;, and &#x60;Failed&#x60;.  | 
**result** | **str** | The callback message result. Possible values include &#x60;ok&#x60; and &#x60;deny&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.callback_message import CallbackMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackMessage from a JSON string
callback_message_instance = CallbackMessage.from_json(json)
# print the JSON string representation of the object
print(CallbackMessage.to_json())

# convert the object into a dict
callback_message_dict = callback_message_instance.to_dict()
# create an instance of CallbackMessage from a dict
callback_message_from_dict = CallbackMessage.from_dict(callback_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


