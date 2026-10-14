# PaymentBulkSendItemUpdateEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBankWithdrawal&#x60;: The payment bank withdrawal event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;PaymentBulkSendItem&#x60;: The payment bulk send item event data. - &#x60;PaymentTopUpUpdate&#x60;: The payment top-up update event data. - &#x60;PaymentOrderUpdate&#x60;: The payment order update event data. - &#x60;PaymentRefundUpdate&#x60;: The payment refund update event data. - &#x60;PaymentPayoutUpdate&#x60;: The payment payout update event data. - &#x60;PaymentBulkSendUpdate&#x60;: The payment bulk send update event data. - &#x60;PaymentBulkSendItemUpdate&#x60;: The payment bulk send item update event data. - &#x60;PaymentAccountBalanceUpdate&#x60;: The Payments account balance updated event data, including account information and balance change details. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. - &#x60;Organization&#x60;: The organization event data. - &#x60;FiatTransaction&#x60;: The fiat transaction event data. | 
**bulk_send_item_id** | **str** | The bulk send item ID. | 
**bulk_send_id** | **str** | The ID of the bulk send that contains this item. | 
**request_id** | **str** | The request ID for the item. | 
**status** | [**PaymentBulkSendItemStatus**](PaymentBulkSendItemStatus.md) |  | 
**requested_amount** | [**PaymentAssetAmount**](PaymentAssetAmount.md) |  | 
**receiving_address** | **str** | The receiving address of the payout item. | 
**tx_hash** | **str** | The blockchain transaction hash. | 
**source_account** | **str** | The Payments account from which the funds are debited: the merchant ID for a merchant account, or &#x60;developer&#x60; for the developer account. | 
**description** | **str** | The description of the payout item. | 
**failed_reason** | [**PaymentFailedReason**](PaymentFailedReason.md) |  | 
**created_timestamp** | **int** | The created time of the bulk send item, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the bulk send item, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_bulk_send_item_update_event_data import PaymentBulkSendItemUpdateEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBulkSendItemUpdateEventData from a JSON string
payment_bulk_send_item_update_event_data_instance = PaymentBulkSendItemUpdateEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentBulkSendItemUpdateEventData.to_json())

# convert the object into a dict
payment_bulk_send_item_update_event_data_dict = payment_bulk_send_item_update_event_data_instance.to_dict()
# create an instance of PaymentBulkSendItemUpdateEventData from a dict
payment_bulk_send_item_update_event_data_from_dict = PaymentBulkSendItemUpdateEventData.from_dict(payment_bulk_send_item_update_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


