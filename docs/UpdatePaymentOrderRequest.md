# UpdatePaymentOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired** | **bool** | Whether to manually expire the order. If set to &#x60;true&#x60;, the order status will be updated to &#x60;Expired&#x60;. | 

## Example

```python
from cobo_waas2.models.update_payment_order_request import UpdatePaymentOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentOrderRequest from a JSON string
update_payment_order_request_instance = UpdatePaymentOrderRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentOrderRequest.to_json())

# convert the object into a dict
update_payment_order_request_dict = update_payment_order_request_instance.to_dict()
# create an instance of UpdatePaymentOrderRequest from a dict
update_payment_order_request_from_dict = UpdatePaymentOrderRequest.from_dict(update_payment_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


