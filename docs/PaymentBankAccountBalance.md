# PaymentBankAccountBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_id** | **str** | The destination bank account ID. | 
**currency** | **str** | The fiat currency of the bank account. | 
**total_balance** | **str** | The total balance of the bank account. | 
**available_balance** | **str** | The available balance of the bank account. | 
**locked_balance** | **str** | The locked balance of the bank account. | 

## Example

```python
from cobo_waas2.models.payment_bank_account_balance import PaymentBankAccountBalance

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBankAccountBalance from a JSON string
payment_bank_account_balance_instance = PaymentBankAccountBalance.from_json(json)
# print the JSON string representation of the object
print(PaymentBankAccountBalance.to_json())

# convert the object into a dict
payment_bank_account_balance_dict = payment_bank_account_balance_instance.to_dict()
# create an instance of PaymentBankAccountBalance from a dict
payment_bank_account_balance_from_dict = PaymentBankAccountBalance.from_dict(payment_bank_account_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


