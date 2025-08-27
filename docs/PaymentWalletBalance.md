# PaymentWalletBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The unique identifier of the wallet. | 
**token_id** | **str** | The ID of the cryptocurrency. | 
**swept_balance** | **str** | The payment wallet swept balance. | [optional] 
**available_balance** | **str** | The payment wallet available balance. | [optional] 
**total_balance** | **str** | The payment wallet total balance. | [optional] 
**above_sweep_threshold_balance** | **str** | The payment wallet above sweep threshold balance. | [optional] 

## Example

```python
from cobo_waas2.models.payment_wallet_balance import PaymentWalletBalance

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWalletBalance from a JSON string
payment_wallet_balance_instance = PaymentWalletBalance.from_json(json)
# print the JSON string representation of the object
print(PaymentWalletBalance.to_json())

# convert the object into a dict
payment_wallet_balance_dict = payment_wallet_balance_instance.to_dict()
# create an instance of PaymentWalletBalance from a dict
payment_wallet_balance_from_dict = PaymentWalletBalance.from_dict(payment_wallet_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


