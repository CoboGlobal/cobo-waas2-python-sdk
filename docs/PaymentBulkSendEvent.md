# PaymentBulkSendEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
**bulk_send_id** | **str** | The bulk send ID. | 
**source_account** | **str** | The source account from which the bulk send will be made. - If the source account is a merchant account, provide the merchant&#39;s ID (e.g., \&quot;M1001\&quot;). - If the source account is the developer account, use the string &#x60;\&quot;developer\&quot;&#x60;.  | 
**description** | **str** | The description for the entire bulk send batch. | [optional] 
**execution_mode** | [**PaymentBulkSendExecutionMode**](PaymentBulkSendExecutionMode.md) |  | 
**status** | [**PaymentBulkSendStatus**](PaymentBulkSendStatus.md) |  | 
**created_timestamp** | **int** | The created time of the bulk send, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the bulk send, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_bulk_send_event import PaymentBulkSendEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBulkSendEvent from a JSON string
payment_bulk_send_event_instance = PaymentBulkSendEvent.from_json(json)
# print the JSON string representation of the object
print(PaymentBulkSendEvent.to_json())

# convert the object into a dict
payment_bulk_send_event_dict = payment_bulk_send_event_instance.to_dict()
# create an instance of PaymentBulkSendEvent from a dict
payment_bulk_send_event_from_dict = PaymentBulkSendEvent.from_dict(payment_bulk_send_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


