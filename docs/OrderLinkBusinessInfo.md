# OrderLinkBusinessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_ids** | **List[str]** | List of supported cryptocurrency token IDs for this payment. Each token ID must be from the supported values.  | 
**custom_exchange_rates** | [**List[OrderLinkBusinessInfoCustomExchangeRatesInner]**](OrderLinkBusinessInfoCustomExchangeRatesInner.md) | Optional list of final exchange rates for different tokens. If provided, these rates will be used instead of real-time market rates.  | [optional] 
**currency** | **str** | The currency for the base order amount and the developer fee. Currently, only &#x60;USD&#x60;/&#x60;USDT&#x60;/&#x60;USDC&#x60; are supported.  | 
**fee_amount** | **str** | The developer fee for the order, in the currency specified by &#x60;currency&#x60;. If &#x60;currency&#x60; is not specified, the fee is in the cryptocurrency specified by &#x60;token_id&#x60;.  If you are a merchant directly serving payers, set this field to &#x60;0&#x60;. Developer fees are only relevant for platforms like payment service providers (PSPs) that charge fees to their downstream merchants.  The developer fee is added to the base amount (&#x60;order_amount&#x60;) to determine the final charge. For example: - Base amount (&#x60;order_amount&#x60;): \&quot;100.00\&quot; - Developer fee (&#x60;fee_amount&#x60;): \&quot;2.00\&quot;  - Total charged to customer: \&quot;102.00\&quot;  Values can contain up to two decimal places.  | 
**merchant_id** | **str** | The merchant ID. | 
**order_amount** | **str** | The base amount of the order, excluding the developer fee (specified in &#x60;fee_amount&#x60;), in the currency specified by &#x60;currency&#x60;. If &#x60;currency&#x60; is not specified, the amount is in the cryptocurrency specified by &#x60;token_id&#x60;.   Values must be greater than &#x60;0&#x60; and contain two decimal places.   | 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. The code should have a maximum length of 128 characters. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by you as a developer to identify this order in your system. This code must be unique across all orders in your system. The code should have a maximum length of 128 characters.  | 
**expired_in** | **int** | The number of seconds until the pay-in order expires, counted from when the request is sent. For example, if set to &#x60;1800&#x60;, the order will expire in 30 minutes. Must be greater than zero and cannot exceed 3 hours (10800 seconds). After expiration:  - The order status becomes final and cannot be changed - The &#x60;received_token_amount&#x60; field will no longer be updated - Funds received after expiration will be categorized as late payments and can only be settled from the developer balance. - A late payment will trigger a &#x60;transactionLate&#x60; webhook event.  | [optional] [default to 1800]
**use_dedicated_address** | **bool** | Whether to allocate a dedicated address for this order.  - &#x60;true&#x60;: A dedicated address will be allocated for this order. - &#x60;false&#x60;: A shared address from the address pool will be used.  | [optional] 
**amount_tolerance** | **str** | Allowed amount deviation, precision to 1 decimal place. | [optional] 

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


