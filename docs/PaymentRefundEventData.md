# PaymentRefundEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
**request_id** | **str** | The request ID provided by you when creating the refund request. | [optional] 
**refund_id** | **str** | The refund order ID. | 
**order_id** | **str** | The ID of the pay-in order corresponding to this refund. | [optional] 
**merchant_id** | **str** | The merchant ID. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency used for refund. | 
**chain_id** | **str** | The ID of the blockchain network on which the refund transaction occurs. | 
**amount** | **str** | The amount in cryptocurrency to be returned for this refund order. | 
**to_address** | **str** | The recipient&#39;s wallet address where the refund will be sent. | 
**status** | [**RefundStatus**](RefundStatus.md) |  | 
**refund_type** | [**RefundType**](RefundType.md) |  | [optional] 
**created_timestamp** | **int** | The creation time of the refund order, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the refund order, represented as a UNIX timestamp in seconds. | [optional] 
**initiator** | **str** |  The initiator of this settlement request. Can return either an API key or the Payments App&#39;s ID.  - Format &#x60;api_key_&lt;API_KEY&gt;&#x60;: Indicates the settlement request was initiated via the Payments API using the API key. - Format &#x60;app_&lt;APP_ID&gt;&#x60;: Indicates the settlement request was initiated through the Payments App using the App ID.  | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of transactions associated with this refund order. Each transaction represents a separate blockchain operation related to the refund process. | [optional] 
**charge_merchant_fee** | **bool** | Whether to charge developer fee to the merchant for the refund.    - &#x60;true&#x60;: The fee amount (specified in &#x60;merchant_fee_amount&#x60;) will be deducted from the merchant&#39;s balance and added to the developer&#39;s balance    - &#x60;false&#x60;: The merchant is not charged any developer fee.  | [optional] 
**merchant_fee_amount** | **str** | The developer fee amount to charge the merchant, denominated in the cryptocurrency specified by &#x60;merchant_fee_token_id&#x60;. This is only applicable if &#x60;charge_merchant_fee&#x60; is set to &#x60;true&#x60;. | [optional] 
**merchant_fee_token_id** | **str** | The ID of the cryptocurrency used for the developer fee. This is only applicable if &#x60;charge_merchant_fee&#x60; is set to true. | [optional] 
**commission_fee** | [**CommissionFee**](CommissionFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payment_refund_event_data import PaymentRefundEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundEventData from a JSON string
payment_refund_event_data_instance = PaymentRefundEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentRefundEventData.to_json())

# convert the object into a dict
payment_refund_event_data_dict = payment_refund_event_data_instance.to_dict()
# create an instance of PaymentRefundEventData from a dict
payment_refund_event_data_from_dict = PaymentRefundEventData.from_dict(payment_refund_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


