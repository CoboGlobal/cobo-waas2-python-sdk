# PaymentPayoutAddressTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | The type of the payout target. | 
**address** | **str** | The recipient address. | 
**chain_id** | **str** | The chain ID of the recipient address. | 

## Example

```python
from cobo_waas2.models.payment_payout_address_target import PaymentPayoutAddressTarget

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPayoutAddressTarget from a JSON string
payment_payout_address_target_instance = PaymentPayoutAddressTarget.from_json(json)
# print the JSON string representation of the object
print(PaymentPayoutAddressTarget.to_json())

# convert the object into a dict
payment_payout_address_target_dict = payment_payout_address_target_instance.to_dict()
# create an instance of PaymentPayoutAddressTarget from a dict
payment_payout_address_target_from_dict = PaymentPayoutAddressTarget.from_dict(payment_payout_address_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


