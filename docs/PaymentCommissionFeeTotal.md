# PaymentCommissionFeeTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | **str** | The commission fee amount. | 

## Example

```python
from cobo_waas2.models.payment_commission_fee_total import PaymentCommissionFeeTotal

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCommissionFeeTotal from a JSON string
payment_commission_fee_total_instance = PaymentCommissionFeeTotal.from_json(json)
# print the JSON string representation of the object
print(PaymentCommissionFeeTotal.to_json())

# convert the object into a dict
payment_commission_fee_total_dict = payment_commission_fee_total_instance.to_dict()
# create an instance of PaymentCommissionFeeTotal from a dict
payment_commission_fee_total_from_dict = PaymentCommissionFeeTotal.from_dict(payment_commission_fee_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


