# OrderLinkBusinessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. The code should have a maximum length of 128 characters. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by you as a developer to identify this order in your system. This code must be unique across all orders in your system. The code should have a maximum length of 128 characters.  | 
**pricing_currency** | **str** | The pricing currency that denominates &#x60;pricing_amount&#x60; and &#x60;fee_amount&#x60;. Currently, only &#x60;USD&#x60;/&#x60;USDT&#x60;/&#x60;USDC&#x60; are supported. This field is required.  | [optional] 
**pricing_amount** | **str** | The base amount of the order, excluding the developer fee (specified in &#x60;fee_amount&#x60;). Values must be greater than &#x60;0&#x60; and contain two decimal places.  | [optional] 
**fee_amount** | **str** | The developer fee for the order. It is added to the base amount (&#x60;pricing_amount&#x60;) to determine the final charge. For example, if &#x60;pricing_amount&#x60; is \&quot;100.00\&quot; and &#x60;fee_amount&#x60; is \&quot;2.00\&quot;, the payer will be charged \&quot;102.00\&quot; in total, with \&quot;100.00\&quot; being settled to the merchant account and \&quot;2.00\&quot; settled to the developer account. Values must be greater than 0 and contain two decimal places.  | 
**payable_currencies** | **List[str]** | The IDs of the cryptocurrencies used for payment. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60;  - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | [optional] 
**payable_amounts** | [**List[OrderLinkBusinessInfoPayableAmountsInner]**](OrderLinkBusinessInfoPayableAmountsInner.md) | The total amounts the payer needs to pay for each currency in &#x60;payable_currencies&#x60;. If this field is left blank, the system will automatically calculate the amounts at order creation using the following formula: (&#x60;pricing_amount&#x60; + &#x60;fee_amount&#x60;) / current exchange rate.  Values must be greater than 0 and contain two decimal places.  | [optional] 
**expired_in** | **int** | The number of seconds until the pay-in order expires, counted from when the request is sent. For example, if set to &#x60;1800&#x60;, the order will expire in 30 minutes. Must be greater than zero and cannot exceed 3 hours (10800 seconds). After expiration:  - The order status becomes final and cannot be changed - The &#x60;received_token_amount&#x60; field will no longer be updated - Funds received after expiration will be categorized as late payments and can only be settled from the developer balance. - A late payment will trigger a &#x60;transactionLate&#x60; webhook event.  | [optional] [default to 1800]
**amount_tolerance** | **str** | The allowed amount deviation, with precision up to 1 decimal place.  For example, if &#x60;payable_amount&#x60; is &#x60;100.00&#x60; and &#x60;amount_tolerance&#x60; is &#x60;0.50&#x60;: - Payer pays 99.55 → Success (difference of 0.45 ≤ 0.5) - Payer pays 99.40 → Underpaid (difference of 0.60 &gt; 0.5)  | [optional] 
**currency** | **str** | This field has been deprecated. Please use &#x60;pricing_currency&#x60; instead. | [optional] 
**order_amount** | **str** | This field has been deprecated. Please use &#x60;pricing_amount&#x60; instead. | [optional] 
**token_ids** | **List[str]** | This field has been deprecated. Please use &#x60;payable_currencies&#x60; instead.  | [optional] 
**custom_exchange_rates** | [**List[OrderLinkBusinessInfoCustomExchangeRatesInner]**](OrderLinkBusinessInfoCustomExchangeRatesInner.md) | This field has been deprecated.  | [optional] 
**use_dedicated_address** | **bool** | This field has been deprecated. | [optional] 

## Example

```python
from cobo_waas2.models.order_link_business_info import OrderLinkBusinessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLinkBusinessInfo from a JSON string
order_link_business_info_instance = OrderLinkBusinessInfo.from_json(json)
# print the JSON string representation of the object
print(OrderLinkBusinessInfo.to_json())

# convert the object into a dict
order_link_business_info_dict = order_link_business_info_instance.to_dict()
# create an instance of OrderLinkBusinessInfo from a dict
order_link_business_info_from_dict = OrderLinkBusinessInfo.from_dict(order_link_business_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


