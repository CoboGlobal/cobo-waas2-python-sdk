# PaymentPayoutRecipientInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The recipient&#39;s wallet address where the payout will be sent. | [optional] 
**token_id** | **str** | The token ID for the cryptocurrency to be sent to the recipient.  If &#x60;recipient_info.token_id&#x60; is on a different chain than &#x60;payout_param.token_id&#x60;, the token will be automatically bridged to the chain specified in &#x60;recipient_info.token_id&#x60;.  | [optional] 
**currency** | **str** | The fiat currency of the bank account to which the payout will be sent. | [optional] 
**bank_account_id** | **str** | The ID of the bank account to which the payout will be sent. You can retrieve the bank account ID by calling [List destination entries](https://www.cobo.com/payments/en/api-references/payment/list-destination-entries). | [optional] 

## Example

```python
from cobo_waas2.models.payment_payout_recipient_info import PaymentPayoutRecipientInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPayoutRecipientInfo from a JSON string
payment_payout_recipient_info_instance = PaymentPayoutRecipientInfo.from_json(json)
# print the JSON string representation of the object
print(PaymentPayoutRecipientInfo.to_json())

# convert the object into a dict
payment_payout_recipient_info_dict = payment_payout_recipient_info_instance.to_dict()
# create an instance of PaymentPayoutRecipientInfo from a dict
payment_payout_recipient_info_from_dict = PaymentPayoutRecipientInfo.from_dict(payment_payout_recipient_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


