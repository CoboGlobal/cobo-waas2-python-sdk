# RetryPaymentCallbacks201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retried** | **bool** | Whether the callback retry request was processed. - &#x60;true&#x60;: The request was processed. This does not guarantee that any callback message was resent or approved, or that the business record has continued processing. - &#x60;false&#x60;: The request was not processed.  | 

## Example

```python
from cobo_waas2.models.retry_payment_callbacks201_response import RetryPaymentCallbacks201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentCallbacks201Response from a JSON string
retry_payment_callbacks201_response_instance = RetryPaymentCallbacks201Response.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentCallbacks201Response.to_json())

# convert the object into a dict
retry_payment_callbacks201_response_dict = retry_payment_callbacks201_response_instance.to_dict()
# create an instance of RetryPaymentCallbacks201Response from a dict
retry_payment_callbacks201_response_from_dict = RetryPaymentCallbacks201Response.from_dict(retry_payment_callbacks201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


