# PaymentEstimateFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency you want to OffRamp settle. | 
**amount** | **str** | The OffRamp settlement amount.  | 

## Example

```python
from cobo_waas2.models.payment_estimate_fee import PaymentEstimateFee

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEstimateFee from a JSON string
payment_estimate_fee_instance = PaymentEstimateFee.from_json(json)
# print the JSON string representation of the object
print(PaymentEstimateFee.to_json())

# convert the object into a dict
payment_estimate_fee_dict = payment_estimate_fee_instance.to_dict()
# create an instance of PaymentEstimateFee from a dict
payment_estimate_fee_from_dict = PaymentEstimateFee.from_dict(payment_estimate_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


