# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The unique identifier of the payment order. Cobo assigns this ID when the payment order is created — when that happens depends on which pay-in method you use.  For the direct method, &#x60;Create pay-in order&#x60; creates the order synchronously and returns &#x60;order_id&#x60; in the response immediately.  For the payment link method, &#x60;Create order link&#x60; returns only the hosted link details and does not create an order, so &#x60;order_id&#x60; does not exist yet at that point. &#x60;order_id&#x60; becomes available only after the payer opens the hosted payment page, selects the payment token and blockchain network, and submits the order — Cobo creates the order and assigns &#x60;order_id&#x60; at that moment, not when the link itself was generated.  | 
**merchant_id** | **str** | The merchant ID. | [optional] 
**merchant_order_code** | **str** | The downstream merchant&#39;s order reference, exactly as you supplied it in &#x60;merchant_order_code&#x60; when creating the order, if you provided one. Present only when a &#x60;merchant_order_code&#x60; was included at order creation. | [optional] 
**psp_order_code** | **str** | The order identifier for your own internal business order, exactly as you supplied it in &#x60;psp_order_code&#x60; when creating the order. This value is unique within your Cobo organization. | 
**pricing_currency** | **str** | The pricing currency of the order. | [optional] 
**pricing_amount** | **str** | The base amount of the order, excluding the developer fee (specified in &#x60;fee_amount&#x60;). | [optional] 
**fee_amount** | **str** | The order-level developer charge credited to your developer balance when the order settles. A value of &#x60;0&#x60; means that no developer fee was charged and the merchant was credited with the full collected amount.  When the collected payment exactly matches the payable amount, the merchant balance is credited with the payable amount minus &#x60;fee_amount&#x60;, and your developer balance is credited with &#x60;fee_amount&#x60;. For example, for a payable amount of &#x60;104.08&#x60; and a &#x60;fee_amount&#x60; of &#x60;2&#x60;, the merchant receives &#x60;102.08&#x60; and you receive &#x60;2&#x60;.  For related fee settings and settlement details, see [Merchant management](https://www.cobo.com/payments/en/guides/merchants) and [Accounts and fund allocation](https://www.cobo.com/payments/en/guides/amounts-and-balances).  | 
**payable_currency** | **str** | The ID of the cryptocurrency used for payment. | [optional] 
**chain_id** | **str** | The ID of the blockchain network where the payment transaction should be made. | 
**payable_amount** | **str** | The cryptocurrency amount to be paid for this order. | 
**exchange_rate** | **str** | The exchange rate between &#x60;payable_currency&#x60; and &#x60;pricing_currency&#x60;, calculated as (&#x60;pricing_amount&#x60; + &#x60;fee_amount&#x60;) / &#x60;payable_amount&#x60;.    &lt;Note&gt;This field is only returned when &#x60;payable_amount&#x60; was not provided in the order creation request. &lt;/Note&gt;  | 
**amount_tolerance** | **str** | The allowed amount deviation, with precision up to 1 decimal place.  For example, if &#x60;payable_amount&#x60; is &#x60;100.00&#x60; and &#x60;amount_tolerance&#x60; is &#x60;0.50&#x60;: - Payer pays 99.55 → Success (difference of 0.45 ≤ 0.5) - Payer pays 99.40 → Underpaid (difference of 0.60 &gt; 0.5)  | [optional] 
**receive_address** | **str** | The recipient wallet address to be used for the payment transaction. | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**received_token_amount** | **str** | The total cryptocurrency amount received for this order. Updates until the expiration time. Precision matches the token standard (e.g., 6 decimals for USDT). | 
**expired_at** | **int** | The expiration time of the pay-in order, represented as a UNIX timestamp in seconds. | [optional] 
**created_timestamp** | **int** | The created time of the order, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The updated time of the order, represented as a UNIX timestamp in seconds. | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of transactions associated with this pay-in order. Each transaction represents a separate blockchain operation related to the settlement process. | [optional] 
**currency** | **str** | This field has been deprecated. Please use &#x60;pricing_currency&#x60; instead. | [optional] 
**order_amount** | **str** | This field has been deprecated. Please use &#x60;pricing_amount&#x60; instead. | [optional] 
**token_id** | **str** | This field has been deprecated. Please use &#x60;payable_currency&#x60; instead. | [optional] 
**settlement_status** | [**SettleStatus**](SettleStatus.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


