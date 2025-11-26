# CreatePaymentOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. This ID is assigned by Cobo when you create the merchant. | 
**token_id** | **str** | The ID of the cryptocurrency used for payment. Supported values:    - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**currency** | **str** | The fiat currency for the base order amount and the developer fee. If left empty, both &#x60;order_amount&#x60; and &#x60;fee_amount&#x60; will be denominated in the cryptocurrency specified by &#x60;token_id&#x60;  Currently, only &#x60;USD&#x60; is supported.  | [optional] [default to '']
**order_amount** | **str** |  The base amount of the order, excluding the developer fee (specified in &#x60;fee_amount&#x60;). The denomination of the amount depends on if &#x60;currency&#x60; is specified: - If &#x60;currency&#x60; is specified, the amount is in the currency specified by &#x60;currency&#x60;, e.g. \&quot;USD\&quot;. - If &#x60;currency&#x60; is not specified, the amount is in the cryptocurrency specified by &#x60;token_id&#x60;, e.g. \&quot;ETH_USDT\&quot;.   Values must be greater than &#x60;0&#x60; and contain two decimal places.  | 
**fee_amount** | **str** |  The developer fee for the order.  - **When to set:**     If you are a merchant serving payers directly, set this field to &#x60;0&#x60;.     Developer fees are only relevant for platforms like payment service providers (PSPs) that charge fees to their downstream merchants.   For details, see [Funds allocation and balances](https://www.cobo.com/developers/v2/payments/amounts-and-balances).  - **Denomination:**     The denomination of &#x60;fee_amount&#x60; depends on the presence of &#x60;currency&#x60;:       - If &#x60;currency&#x60; is set, the amount is denominated in that currency (e.g., \&quot;USD\&quot;).       - If &#x60;currency&#x60; is not set, the amount is denominated in the cryptocurrency specified by &#x60;token_id&#x60; (e.g., \&quot;ETH_USDT\&quot;).  - **Calculation:**     The developer fee is added to the base order amount (&#x60;order_amount&#x60;) to determine the final amount charged to the customer.     For example:       - Base amount (&#x60;order_amount&#x60;): \&quot;100.00\&quot;       - Developer fee (&#x60;fee_amount&#x60;): \&quot;2.00\&quot;       - **Total charged:** \&quot;102.00\&quot;  - **Formatting:**     The value can contain up to two decimal places.  | 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. The code should have a maximum length of 128 characters. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by you as a developer to identify this order in your system. This code must be unique across all orders in your system. The code should have a maximum length of 128 characters.  | 
**expired_in** | **int** | The number of seconds until the pay-in order expires, counted from when the request is sent. For example, if set to &#x60;1800&#x60;, the order will expire in 30 minutes. Must be greater than zero and cannot exceed 3 hours (10800 seconds). After expiration:  - The order status becomes final and cannot be changed - The &#x60;received_token_amount&#x60; field will no longer be updated - Funds received after expiration will be categorized as late payments and can only be settled from the developer balance. - A late payment will trigger a &#x60;transactionLate&#x60; webhook event.  | [optional] [default to 1800]
**use_dedicated_address** | **bool** | This field has been deprecated.  | [optional] 
**custom_exchange_rate** | **str** |  A custom exchange rate that defines how much fiat currency equals 1 unit of cryptocurrency. If not provided, the system&#39;s default exchange rate will be used.  For example, if the fiat currency is USD and the cryptocurrency is USDT, setting &#x60;custom_exchange_rate&#x60; to &#x60;\&quot;0.99\&quot;&#x60; means that 1 USDT will be valued at 0.99 USD.  | [optional] 
**amount_tolerance** | **str** | The maximum allowed deviation from the payable amount in the case of underpayment, specified as a positive value with up to one decimal place. If you provide more than one decimal place, an error will occur.  When the actual received amount is within this deviation (inclusive) of the payable amount, the order status will be set to &#x60;Completed&#x60; rather than &#x60;Underpaid&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.create_payment_order_request import CreatePaymentOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentOrderRequest from a JSON string
create_payment_order_request_instance = CreatePaymentOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentOrderRequest.to_json())

# convert the object into a dict
create_payment_order_request_dict = create_payment_order_request_instance.to_dict()
# create an instance of CreatePaymentOrderRequest from a dict
create_payment_order_request_from_dict = CreatePaymentOrderRequest.from_dict(create_payment_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


