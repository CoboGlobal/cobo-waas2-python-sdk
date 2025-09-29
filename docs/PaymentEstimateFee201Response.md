# PaymentEstimateFee201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PaymentEstimatedFee]**](PaymentEstimatedFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payment_estimate_fee201_response import PaymentEstimateFee201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEstimateFee201Response from a JSON string
payment_estimate_fee201_response_instance = PaymentEstimateFee201Response.from_json(json)
# print the JSON string representation of the object
print(PaymentEstimateFee201Response.to_json())

# convert the object into a dict
payment_estimate_fee201_response_dict = payment_estimate_fee201_response_instance.to_dict()
# create an instance of PaymentEstimateFee201Response from a dict
payment_estimate_fee201_response_from_dict = PaymentEstimateFee201Response.from_dict(payment_estimate_fee201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


