# PaymentEstimatedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID for which fees will be calculated. | 
**amount** | **str** | The transaction amount for which fees will be calculated. | 
**commission_fee** | [**CommissionFee**](CommissionFee.md) |  | [optional] 
**bridging_fee** | [**BridgingFee**](BridgingFee.md) |  | [optional] 
**otc_fee** | [**OtcFee**](OtcFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payment_estimated_fee import PaymentEstimatedFee

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEstimatedFee from a JSON string
payment_estimated_fee_instance = PaymentEstimatedFee.from_json(json)
# print the JSON string representation of the object
print(PaymentEstimatedFee.to_json())

# convert the object into a dict
payment_estimated_fee_dict = payment_estimated_fee_instance.to_dict()
# create an instance of PaymentEstimatedFee from a dict
payment_estimated_fee_from_dict = PaymentEstimatedFee.from_dict(payment_estimated_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


