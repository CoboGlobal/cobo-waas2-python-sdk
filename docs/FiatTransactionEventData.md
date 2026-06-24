# FiatTransactionEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;PaymentAccountBalanceUpdate&#x60;: The Payments account balance updated event data, including account information and balance change details. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. - &#x60;Organization&#x60;: The organization event data. - &#x60;FiatTransaction&#x60;: The fiat transaction event data. | 
**transaction_id** | **str** | The transaction ID. | 
**main_transaction_id** | **str** | The UUID of the parent (main) transaction that this record is associated with. Set only when the current record is a gas/fee transaction initiated by FeeStation; omit for main transactions. | [optional] 
**transaction_type** | [**FeeStationFiatTransactionType**](FeeStationFiatTransactionType.md) |  | 
**amount** | **str** | The transaction amount. | 
**fiat_currency** | **str** | The fiat currency of the transaction. Possible values include:   - &#x60;USD&#x60;: US Dollar.  | 
**status** | **str** | The status of the fiat transaction. Possible values include:   - &#x60;Created&#x60;: The transaction has been created.   - &#x60;Succeeded&#x60;: The transaction has been completed successfully.  | 
**cobo_category** | **List[str]** | The Cobo category of the transaction. | [optional] 
**created_timestamp** | **int** | The time when the transaction was created, in Unix timestamp format, measured in milliseconds. | [optional] 
**modified_timestamp** | **int** | The time when the transaction was last modified, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.fiat_transaction_event_data import FiatTransactionEventData

# TODO update the JSON string below
json = "{}"
# create an instance of FiatTransactionEventData from a JSON string
fiat_transaction_event_data_instance = FiatTransactionEventData.from_json(json)
# print the JSON string representation of the object
print(FiatTransactionEventData.to_json())

# convert the object into a dict
fiat_transaction_event_data_dict = fiat_transaction_event_data_instance.to_dict()
# create an instance of FiatTransactionEventData from a dict
fiat_transaction_event_data_from_dict = FiatTransactionEventData.from_dict(fiat_transaction_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


