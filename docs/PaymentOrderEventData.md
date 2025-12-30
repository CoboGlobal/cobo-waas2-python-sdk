# PaymentOrderEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
**order_id** | **str** | The order ID. | 
**merchant_id** | **str** | The merchant ID. | [optional] 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by the developer to identify this order in their system. | 
**pricing_currency** | **str** | The pricing currency of the order. | [optional] 
**pricing_amount** | **str** | The base amount of the order, excluding the developer fee (specified in &#x60;fee_amount&#x60;). | [optional] 
**fee_amount** | **str** | The developer fee for the order. It is added to the base amount to determine the final charge. | 
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
from cobo_waas2.models.payment_order_event_data import PaymentOrderEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOrderEventData from a JSON string
payment_order_event_data_instance = PaymentOrderEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentOrderEventData.to_json())

# convert the object into a dict
payment_order_event_data_dict = payment_order_event_data_instance.to_dict()
# create an instance of PaymentOrderEventData from a dict
payment_order_event_data_from_dict = PaymentOrderEventData.from_dict(payment_order_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


