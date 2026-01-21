# PaymentTransactionEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
**transaction_id** | **str** | The transaction ID. | 
**cobo_id** | **str** | The Cobo ID, which can be used to track a transaction. | [optional] 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 
**wallet_id** | **str** | For deposit transactions, this property represents the wallet ID of the transaction destination. For transactions of other types, this property represents the wallet ID of the transaction source. | 
**type** | [**TransactionType**](TransactionType.md) |  | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**sub_status** | [**TransactionSubStatus**](TransactionSubStatus.md) |  | [optional] 
**failed_reason** | **str** | (This property is applicable to approval failures and signature failures only) The reason why the transaction failed. | [optional] 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
**source** | [**TransactionSource**](TransactionSource.md) |  | 
**destination** | [**TransactionDestination**](TransactionDestination.md) |  | 
**result** | [**TransactionResult**](TransactionResult.md) |  | [optional] 
**fee** | [**TransactionFee**](TransactionFee.md) |  | [optional] 
**initiator** | **str** | The transaction initiator. | [optional] 
**initiator_type** | [**TransactionInitiatorType**](TransactionInitiatorType.md) |  | 
**confirmed_num** | **int** | The number of confirmations this transaction has received. | [optional] 
**confirming_threshold** | **int** | The minimum number of confirmations required to deem a transaction secure. The common threshold is 6 for a Bitcoin transaction. | [optional] 
**transaction_hash** | **str** | The transaction hash. | [optional] 
**block_info** | [**TransactionBlockInfo**](TransactionBlockInfo.md) |  | [optional] 
**raw_tx_info** | [**TransactionRawTxInfo**](TransactionRawTxInfo.md) |  | [optional] 
**replacement** | [**TransactionReplacement**](TransactionReplacement.md) |  | [optional] 
**category** | **List[str]** | A custom transaction category for you to identify your transfers more easily. | [optional] 
**description** | **str** | The description for your transaction. | [optional] 
**is_loop** | **bool** | Whether the transaction was executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer. - &#x60;true&#x60;: The transaction was executed as a Cobo Loop transfer. - &#x60;false&#x60;: The transaction was not executed as a Cobo Loop transfer.  | [optional] 
**cobo_category** | **List[str]** | The transaction category defined by Cobo. For more details, refer to [Cobo-defined categories](/v2/guides/transactions/manage-transactions#cobo-defined-categories).  | [optional] 
**extra** | **List[str]** | A list of JSON-encoded strings containing structured, business-specific extra information for the transaction. Each item corresponds to a specific data type, indicated by the &#x60;extra_type&#x60; field in the JSON object (for example, \&quot;BabylonBusinessInfo\&quot;, \&quot;BtcAddressInfo\&quot;).  | [optional] 
**fueling_info** | [**TransactionFuelingInfo**](TransactionFuelingInfo.md) |  | [optional] 
**created_timestamp** | **int** | The time when the transaction was created, in Unix timestamp format, measured in milliseconds. | 
**updated_timestamp** | **int** | The time when the transaction was updated, in Unix timestamp format, measured in milliseconds. | 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | 
**order_id** | **str** | The pay-in order ID. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by the developer to identify this order in their system. | [optional] 
**payer_id** | **str** | A unique identifier assigned by Cobo to track and identify individual payers. | [optional] 
**custom_payer_id** | **str** | A unique identifier assigned by the developer to track and identify individual payers in their system. | [optional] 

## Example

```python
from cobo_waas2.models.payment_transaction_event_data import PaymentTransactionEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransactionEventData from a JSON string
payment_transaction_event_data_instance = PaymentTransactionEventData.from_json(json)
# print the JSON string representation of the object
print(PaymentTransactionEventData.to_json())

# convert the object into a dict
payment_transaction_event_data_dict = payment_transaction_event_data_instance.to_dict()
# create an instance of PaymentTransactionEventData from a dict
payment_transaction_event_data_from_dict = PaymentTransactionEventData.from_dict(payment_transaction_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


