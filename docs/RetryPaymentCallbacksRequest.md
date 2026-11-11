# RetryPaymentCallbacksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_type** | [**PaymentCallbackBusinessType**](PaymentCallbackBusinessType.md) |  | 
**business_id** | **str** | The public ID of the business record, determined by &#x60;business_type&#x60;. - &#x60;refund&#x60;: The refund code, returned as &#x60;refund_id&#x60; when you create or retrieve a refund order. For example, &#x60;R20250304-M1001-1001&#x60;. - &#x60;payout&#x60;: The payout ID, returned as &#x60;payout_id&#x60; when you create or retrieve a payout. For example, &#x60;aff0e1cb-15b2-4e1f-9b9d-a9133715986f&#x60;. - &#x60;bulk_send&#x60;: The bulk send ID, returned as &#x60;bulk_send_id&#x60; when you create or retrieve a bulk send. For example, &#x60;123e4567-e89b-42d3-a456-426614174003&#x60;.  Do not provide an internal database ID, request ID, callback message ID, or refund link ID. The business record must belong to your organization.  | 

## Example

```python
from cobo_waas2.models.retry_payment_callbacks_request import RetryPaymentCallbacksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentCallbacksRequest from a JSON string
retry_payment_callbacks_request_instance = RetryPaymentCallbacksRequest.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentCallbacksRequest.to_json())

# convert the object into a dict
retry_payment_callbacks_request_dict = retry_payment_callbacks_request_instance.to_dict()
# create an instance of RetryPaymentCallbacksRequest from a dict
retry_payment_callbacks_request_from_dict = RetryPaymentCallbacksRequest.from_dict(retry_payment_callbacks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


