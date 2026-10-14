# PaymentFailedReason

The structured failure reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The failure code.  | 
**message** | **str** | The failure message. | 

## Example

```python
from cobo_waas2.models.payment_failed_reason import PaymentFailedReason

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFailedReason from a JSON string
payment_failed_reason_instance = PaymentFailedReason.from_json(json)
# print the JSON string representation of the object
print(PaymentFailedReason.to_json())

# convert the object into a dict
payment_failed_reason_dict = payment_failed_reason_instance.to_dict()
# create an instance of PaymentFailedReason from a dict
payment_failed_reason_from_dict = PaymentFailedReason.from_dict(payment_failed_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


