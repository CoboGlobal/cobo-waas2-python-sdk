# PaymentWalletBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The unique identifier of the wallet. | 
**token_id** | **str** | The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. | 
**swept_balance** | **str** | The total amount of the token on the sweep-to address of the payment wallet. | [optional] 
**available_balance** | **str** | The balance available for settlement or refund, in the specified cryptocurrency. | [optional] 
**total_balance** | **str** | The total balance of the token for the payment wallet. | [optional] 
**above_sweep_threshold_balance** | **str** | The total amount of funds that exceed the sweep threshold across all receiving addresses in the payment wallet. When the balance on a receiving address exceeds the sweep threshold, those funds become eligible for automatic sweeping and are included in this balance. | [optional] 

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


