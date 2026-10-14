# PaymentOrderUpdateEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBankWithdrawal&#x60;: The payment bank withdrawal event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;PaymentBulkSendItem&#x60;: The payment bulk send item event data. - &#x60;PaymentTopUpUpdate&#x60;: The payment top-up update event data. - &#x60;PaymentOrderUpdate&#x60;: The payment order update event data. - &#x60;PaymentRefundUpdate&#x60;: The payment refund update event data. - &#x60;PaymentPayoutUpdate&#x60;: The payment payout update event data. - &#x60;PaymentBulkSendUpdate&#x60;: The payment bulk send update event data. - &#x60;PaymentBulkSendItemUpdate&#x60;: The payment bulk send item update event data. - &#x60;PaymentAccountBalanceUpdate&#x60;: The Payments account balance updated event data, including account information and balance change details. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. - &#x60;Organization&#x60;: The organization event data. - &#x60;FiatTransaction&#x60;: The fiat transaction event data. | 
**order_id** | **str** |  The order ID to be included in this settlement.  - If provided: Settles merchant funds received from this specific order - If empty: Settles merchant funds received from all unsettled orders of the specified merchant  **Usage conditions** - Only applicable when &#x60;settlement_type&#x60; is set to &#x60;Merchant&#x60; - Cannot be used together with &#x60;amount&#x60; parameter        | 
**psp_order_code** | **str** | A unique reference code assigned by the developer to identify this order in their system. | 
**merchant_id** | **str** | The merchant ID associated with the order. | 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**notice_type** | [**PaymentOrderNoticeType**](PaymentOrderNoticeType.md) |  | 
**receive_address** | **str** | The recipient wallet address for the payment transaction. | 
**expired_at** | **int** | The expiration time of the pay-in order, represented as a UNIX timestamp in seconds. | 
**requested_amount** | [**PaymentAssetAmount**](PaymentAssetAmount.md) | The requested amount. | 
**credited_amount** | [**PaymentAssetAmount**](PaymentAssetAmount.md) | The credited amount. | 
**outstanding_amount** | [**PaymentAssetAmount**](PaymentAssetAmount.md) | The outstanding amount. | 
**transactions** | [**List[PaymentOrderDeposit]**](PaymentOrderDeposit.md) | The incoming transactions associated with the order. | 
**created_timestamp** | **int** | The created time of the order, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the order, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_order_update_event_data import PaymentOrderUpdateEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOrderUpdateEventData from a JSON string
payment_order_update_event_data_instance = PaymentOrderUpdateEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentOrderUpdateEventData.to_json())

# convert the object into a dict
payment_order_update_event_data_dict = payment_order_update_event_data_instance.to_dict()
# create an instance of PaymentOrderUpdateEventData from a dict
payment_order_update_event_data_from_dict = PaymentOrderUpdateEventData.from_dict(payment_order_update_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


