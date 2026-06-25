# PaymentAccountBalanceUpdateEventData

This event occurs when the available balance of a Payments account changes for a specific token. The balance change fields are aligned with the `PaymentBalanceChange` object returned by

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;PaymentAccountBalanceUpdate&#x60;: The Payments account balance updated event data, including account information and balance change details. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. - &#x60;Organization&#x60;: The organization event data. - &#x60;FiatTransaction&#x60;: The fiat transaction event data. | 
**source_account** | **str** | The source account of the balance change. This field uses the same semantics as &#x60;source_account&#x60; in [List balance changes](https://www.cobo.com/developers/v2/api-references/payment/list-balance-changes). - When the account is a merchant account, this is the merchant ID (merchant code), which you can retrieve by calling [List all merchants](https://www.cobo.com/developers/v2/api-references/payment/list-all-merchants). - When the account is the developer account, use &#x60;developer&#x60;.  | 
**source_id** | **str** | The source ID of the balance change. | 
**source_type** | [**PaymentBalanceChangeSourceType**](PaymentBalanceChangeSourceType.md) |  | 
**token_id** | **str** | The token ID of the balance change. | 
**amount** | **str** | The balance change amount, truncated to two decimal places and represented as a numeric string. | 
**amount_raw** | **str** | The balance change amount in the token&#39;s decimal precision, represented as a numeric string. | 
**balance_before** | **str** | The account balance before the balance change, truncated to two decimal places and represented as a numeric string. | 
**balance_before_raw** | **str** | The account balance before the balance change in the token&#39;s decimal precision, represented as a numeric string. | 
**balance_after** | **str** | The account balance after the balance change, truncated to two decimal places and represented as a numeric string. | 
**balance_after_raw** | **str** | The account balance after the balance change in the token&#39;s decimal precision, represented as a numeric string. | 
**flow_direction** | [**PaymentBalanceFlowDirection**](PaymentBalanceFlowDirection.md) |  | 
**update_time** | **int** | The time when the balance was updated, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_account_balance_update_event_data import PaymentAccountBalanceUpdateEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccountBalanceUpdateEventData from a JSON string
payment_account_balance_update_event_data_instance = PaymentAccountBalanceUpdateEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentAccountBalanceUpdateEventData.to_json())

# convert the object into a dict
payment_account_balance_update_event_data_dict = payment_account_balance_update_event_data_instance.to_dict()
# create an instance of PaymentAccountBalanceUpdateEventData from a dict
payment_account_balance_update_event_data_from_dict = PaymentAccountBalanceUpdateEventData.from_dict(payment_account_balance_update_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


