# MerchantBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**token_id** | **str** | The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. | 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | 
**total_received_amount** | **str** | The total amount of the token that has been received by the merchant. | [optional] 
**settled_amount** | **str** | The total amount of the token that has been paid out from the merchant&#39;s balance. | [optional] 
**payout_amount** | **str** | This field is reserved for future use. | [optional] 
**refunded_amount** | **str** | The total amount of the token that has been refunded from the merchant&#39;s balance. | [optional] 
**total_balance** | **str** |  The current balance of this token available to the merchant for payouts or refunds.  For more information, please refer to [Accounts and fund allocation](https://www.cobo.com/payments/en/guides/amounts-and-balances)  | [optional] 
**available_balance** | **str** | This field has been deprecated.  | [optional] 
**locked_balance** | **str** | This field is reserved for future use. | [optional] 

## Example

```python
from cobo_waas2.models.merchant_balance import MerchantBalance

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBalance from a JSON string
merchant_balance_instance = MerchantBalance.from_json(json)
# print the JSON string representation of the object
print(MerchantBalance.to_json())

# convert the object into a dict
merchant_balance_dict = merchant_balance_instance.to_dict()
# create an instance of MerchantBalance from a dict
merchant_balance_from_dict = MerchantBalance.from_dict(merchant_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


