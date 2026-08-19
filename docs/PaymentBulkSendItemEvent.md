# PaymentBulkSendItemEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBankWithdrawal&#x60;: The payment bank withdrawal event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;PaymentBulkSendItem&#x60;: The payment bulk send item event data. - &#x60;PaymentAccountBalanceUpdate&#x60;: The Payments account balance updated event data, including account information and balance change details. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. - &#x60;Organization&#x60;: The organization event data. - &#x60;FiatTransaction&#x60;: The fiat transaction event data. | 
**bulk_send_item_id** | **str** | The bulk send item ID. | 
**token_id** | **str** | The token ID of the cryptocurrency to be sent to the recipient. | 
**receiving_address** | **str** | The receiving address. | 
**amount** | **str** | The amount of the cryptocurrency to be sent to the recipient. | 
**description** | **str** | A note or comment about the bulk send item. | [optional] 
**tx_hash** | **str** | The transaction hash of the bulk send item. | [optional] 
**status** | [**PaymentBulkSendItemStatus**](PaymentBulkSendItemStatus.md) |  | 
**validation_status** | [**PaymentBulkSendItemValidationStatus**](PaymentBulkSendItemValidationStatus.md) |  | 
**failed_reason** | **str** | The reason why the bulk send item failed. | [optional] 
**bulk_send_id** | **str** | The bulk send ID that this item belongs to. | 
**request_id** | **str** | The request ID of the bulk send batch. | [optional] 
**source_account** | **str** | The source account ID of the bulk send batch. | 
**created_timestamp** | **int** | The created time of the bulk send item, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the bulk send item, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_bulk_send_item_event import PaymentBulkSendItemEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBulkSendItemEvent from a JSON string
payment_bulk_send_item_event_instance = PaymentBulkSendItemEvent.from_json(json)
# print the JSON string representation of the object
print(PaymentBulkSendItemEvent.to_json())

# convert the object into a dict
payment_bulk_send_item_event_dict = payment_bulk_send_item_event_instance.to_dict()
# create an instance of PaymentBulkSendItemEvent from a dict
payment_bulk_send_item_event_from_dict = PaymentBulkSendItemEvent.from_dict(payment_bulk_send_item_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


