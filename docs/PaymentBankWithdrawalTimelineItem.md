# PaymentBankWithdrawalTimelineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PaymentBankWithdrawalStatus**](PaymentBankWithdrawalStatus.md) |  | 
**timestamp** | **int** | The time when the bank withdrawal entered this status, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_bank_withdrawal_timeline_item import PaymentBankWithdrawalTimelineItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBankWithdrawalTimelineItem from a JSON string
payment_bank_withdrawal_timeline_item_instance = PaymentBankWithdrawalTimelineItem.from_json(json)
# print the JSON string representation of the object
print(PaymentBankWithdrawalTimelineItem.to_json())

# convert the object into a dict
payment_bank_withdrawal_timeline_item_dict = payment_bank_withdrawal_timeline_item_instance.to_dict()
# create an instance of PaymentBankWithdrawalTimelineItem from a dict
payment_bank_withdrawal_timeline_item_from_dict = PaymentBankWithdrawalTimelineItem.from_dict(payment_bank_withdrawal_timeline_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


