# RetryCallbackMessage201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retried** | **bool** | Whether the callback message has been successfully resent: - &#x60;true&#x60;: The callback message has been successfully resent. - &#x60;false&#x60;: The callback message has not been successfully resent.  | [optional] 

## Example

```python
from cobo_waas2.models.retry_callback_message201_response import RetryCallbackMessage201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetryCallbackMessage201Response from a JSON string
retry_callback_message201_response_instance = RetryCallbackMessage201Response.from_json(json)
# print the JSON string representation of the object
print(RetryCallbackMessage201Response.to_json())

# convert the object into a dict
retry_callback_message201_response_dict = retry_callback_message201_response_instance.to_dict()
# create an instance of RetryCallbackMessage201Response from a dict
retry_callback_message201_response_from_dict = RetryCallbackMessage201Response.from_dict(retry_callback_message201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


