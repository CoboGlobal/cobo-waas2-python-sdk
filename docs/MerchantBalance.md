# MerchantBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**token_id** | **str** | The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. | 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | 
**total_received_amount** | **str** | The total amount of the token that has been received by the merchant. | [optional] 
**settled_amount** | **str** | The total amount of the token that has been paid out from the merchant&#39;s balance. | [optional] 
**refunded_amount** | **str** | The total amount of the token that has been refunded from the merchant&#39;s balance. | [optional] 
**total_balance** | **str** |  The total balance of the token available for payout or refund for the merchant.  &#x60;total_balance&#x60; &#x3D; &#x60;total_received_amount&#x60; - &#x60;settled_amount&#x60; - &#x60;refunded_amount&#x60;  For more information, please refer to [Amounts and Balances](/v2_cn/payments/amounts-and-balances)  | [optional] 
**available_balance** | **str** | This field has been deprecated. | [optional] 

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


