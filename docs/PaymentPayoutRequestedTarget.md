# PaymentPayoutRequestedTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | The type of the payout target. | 
**address** | **str** | The recipient address. | 
**chain_id** | **str** | The chain ID of the recipient address. | 
**bank_account_id** | **str** | The recipient bank account ID. | 
**account_alias** | **str** | The alias of the recipient bank account. | [optional] 
**bank_name** | **str** | The recipient bank name. | [optional] 
**currency** | **str** | The currency of the recipient bank account. | [optional] 

## Example

```python
from cobo_waas2.models.payment_payout_requested_target import PaymentPayoutRequestedTarget

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPayoutRequestedTarget from a JSON string
payment_payout_requested_target_instance = PaymentPayoutRequestedTarget.from_json(json)
# print the JSON string representation of the object
print(PaymentPayoutRequestedTarget.to_json())

# convert the object into a dict
payment_payout_requested_target_dict = payment_payout_requested_target_instance.to_dict()
# create an instance of PaymentPayoutRequestedTarget from a dict
payment_payout_requested_target_from_dict = PaymentPayoutRequestedTarget.from_dict(payment_payout_requested_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


