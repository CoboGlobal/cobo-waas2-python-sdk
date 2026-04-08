# PaymentEstimateFeeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**PaymentFeeType**](PaymentFeeType.md) |  | [optional] 
**estimate_fees** | [**List[PaymentEstimateFee]**](PaymentEstimateFee.md) | A list of token IDs and amounts for which fees will be calculated. | 
**recipient_token_id** | **str** | The token ID that the recipient will receive. Required only when &#x60;fee_type&#x60; is &#x60;CryptoPayoutBridge&#x60;. | [optional] 
**transfer_via_va** | **bool** | For OffRamp payout, whether the payout is transferred to a registered bank account via a virtual account (VA) or directly. - &#x60;true&#x60;: The payout is transferred to a registered bank account via a VA (virtual account). - &#x60;false&#x60;: The payout is transferred directly to a registered bank account.  | [optional] 

## Example

```python
from cobo_waas2.models.payment_estimate_fee_request import PaymentEstimateFeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentEstimateFeeRequest from a JSON string
payment_estimate_fee_request_instance = PaymentEstimateFeeRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentEstimateFeeRequest.to_json())

# convert the object into a dict
payment_estimate_fee_request_dict = payment_estimate_fee_request_instance.to_dict()
# create an instance of PaymentEstimateFeeRequest from a dict
payment_estimate_fee_request_from_dict = PaymentEstimateFeeRequest.from_dict(payment_estimate_fee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


