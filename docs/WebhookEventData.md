# WebhookEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. - &#x60;PaymentTransaction&#x60;: The payment transaction event data. - &#x60;PaymentAddressUpdate&#x60;: The top-up address update event data. - &#x60;PaymentPayout&#x60;: The payment payout event data. - &#x60;PaymentBulkSend&#x60;: The payment bulk send event data. - &#x60;BalanceUpdateInfo&#x60;: The balance update event data. - &#x60;SuspendedToken&#x60;: The token suspension event data. - &#x60;ComplianceDisposition&#x60;: The compliance disposition event data. - &#x60;ComplianceKytScreenings&#x60;: The compliance KYT screenings event data. - &#x60;ComplianceKyaScreenings&#x60;: The compliance KYA screenings event data. | 
**transaction_id** | **str** | The transaction ID. | 
**cobo_id** | **str** | The Cobo ID, which can be used to track a transaction. | [optional] 
**request_id** | **str** | The request ID provided by you when creating the payout. | 
**wallet_id** | **str** | For deposit transactions, this property represents the wallet ID of the transaction destination. For transactions of other types, this property represents the wallet ID of the transaction source. | 
**type** | [**TransactionType**](TransactionType.md) |  | [optional] 
**status** | [**KyaScreeningStatus**](KyaScreeningStatus.md) |  | 
**sub_status** | [**TransactionSubStatus**](TransactionSubStatus.md) |  | [optional] 
**failed_reason** | **str** | (This property is applicable to approval failures and signature failures only) The reason why the transaction failed. | [optional] 
**chain_id** | **str** | The chain identifier. | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
**source** | [**TransactionSource**](TransactionSource.md) |  | 
**destination** | [**TransactionDestination**](TransactionDestination.md) |  | 
**result** | [**TransactionResult**](TransactionResult.md) |  | [optional] 
**fee** | [**TransactionFee**](TransactionFee.md) |  | [optional] 
**initiator** | **str** | The initiator of this payout, usually the user&#39;s API key. | [optional] 
**initiator_type** | [**TransactionInitiatorType**](TransactionInitiatorType.md) |  | 
**confirmed_num** | **int** | The number of confirmations this transaction has received. | [optional] 
**confirming_threshold** | **int** | The minimum number of confirmations required to deem a transaction secure. The common threshold is 6 for a Bitcoin transaction. | [optional] 
**transaction_hash** | **str** | The transaction hash. | [optional] 
**block_info** | [**TransactionBlockInfo**](TransactionBlockInfo.md) |  | [optional] 
**raw_tx_info** | [**TransactionRawTxInfo**](TransactionRawTxInfo.md) |  | [optional] 
**replacement** | [**TransactionReplacement**](TransactionReplacement.md) |  | [optional] 
**category** | **List[str]** | A custom transaction category for you to identify your transfers more easily. | [optional] 
**description** | **str** | The description for the entire bulk send batch. | [optional] 
**is_loop** | **bool** | Whether the transaction was executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer. - &#x60;true&#x60;: The transaction was executed as a Cobo Loop transfer. - &#x60;false&#x60;: The transaction was not executed as a Cobo Loop transfer.  | [optional] 
**cobo_category** | **List[str]** | The transaction category defined by Cobo. For more details, refer to [Cobo-defined categories](/v2/guides/transactions/manage-transactions#cobo-defined-categories).  | [optional] 
**extra** | **List[str]** | A list of JSON-encoded strings containing structured, business-specific extra information for the transaction. Each item corresponds to a specific data type, indicated by the &#x60;extra_type&#x60; field in the JSON object (for example, \&quot;BabylonBusinessInfo\&quot;, \&quot;BtcAddressInfo\&quot;).  | [optional] 
**fueling_info** | [**TransactionFuelingInfo**](TransactionFuelingInfo.md) |  | [optional] 
**created_timestamp** | **int** | The time when the screening request was created, in Unix timestamp format, measured in milliseconds. | 
**updated_timestamp** | **int** | The time when the screening status was updated, in Unix timestamp format, measured in milliseconds. | 
**tss_request_id** | **str** | The TSS request ID. | [optional] 
**source_key_share_holder_group** | [**SourceGroup**](SourceGroup.md) |  | [optional] 
**target_key_share_holder_group_id** | **str** | The target key share holder group ID. | [optional] 
**addresses** | [**List[AddressesEventDataAllOfAddresses]**](AddressesEventDataAllOfAddresses.md) | A list of addresses. | [optional] 
**wallet** | [**WalletInfo**](WalletInfo.md) |  | [optional] 
**vault_id** | **str** | The vault ID. | [optional] 
**project_id** | **str** | The project ID. | [optional] 
**name** | **str** | The vault name. | [optional] 
**root_pubkeys** | [**List[RootPubkey]**](RootPubkey.md) |  | [optional] 
**chains** | [**List[ChainInfo]**](ChainInfo.md) | The enabled chains. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtypes** | [**List[WalletSubtype]**](WalletSubtype.md) |  | [optional] 
**tokens** | [**List[TokenInfo]**](TokenInfo.md) | The enabled tokens. | 
**contract_address** | **str** | The token&#39;s contract address on the specified blockchain. | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**token** | [**TokenInfo**](TokenInfo.md) |  | [optional] 
**feedback** | **str** | The feedback provided by Cobo when a token listing request is rejected. | [optional] 
**address** | **str** | The screened blockchain address. | 
**wallet_uuid** | **str** | The wallet ID. | 
**balance** | [**Balance**](Balance.md) |  | 
**token_ids** | **str** | A list of token IDs, separated by comma. | 
**operation_type** | [**SuspendedTokenOperationType**](SuspendedTokenOperationType.md) |  | 
**order_id** | **str** | The pay-in order ID. | 
**merchant_id** | **str** | The merchant ID. | [optional] 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by the developer to identify this order in their system. | 
**pricing_currency** | **str** | The pricing currency of the order. | [optional] 
**pricing_amount** | **str** | The base amount of the order, excluding the developer fee (specified in &#x60;fee_amount&#x60;). | [optional] 
**fee_amount** | **str** | The developer fee for the order. It is added to the base amount to determine the final charge. | 
**payable_currency** | **str** | The ID of the cryptocurrency used for payment. | [optional] 
**payable_amount** | **str** | The cryptocurrency amount to be paid for this order. | 
**exchange_rate** | **str** | The exchange rate between &#x60;payable_currency&#x60; and &#x60;pricing_currency&#x60;, calculated as (&#x60;pricing_amount&#x60; + &#x60;fee_amount&#x60;) / &#x60;payable_amount&#x60;.    &lt;Note&gt;This field is only returned when &#x60;payable_amount&#x60; was not provided in the order creation request. &lt;/Note&gt;  | 
**amount_tolerance** | **str** | The allowed amount deviation, with precision up to 1 decimal place.  For example, if &#x60;payable_amount&#x60; is &#x60;100.00&#x60; and &#x60;amount_tolerance&#x60; is &#x60;0.50&#x60;: - Payer pays 99.55 → Success (difference of 0.45 ≤ 0.5) - Payer pays 99.40 → Underpaid (difference of 0.60 &gt; 0.5)  | [optional] 
**receive_address** | **str** | The recipient wallet address to be used for the payment transaction. | 
**received_token_amount** | **str** | The total cryptocurrency amount received for this order. Updates until the expiration time. Precision matches the token standard (e.g., 6 decimals for USDT). | 
**expired_at** | **int** | The expiration time of the pay-in order, represented as a UNIX timestamp in seconds. | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of payout transactions. | [optional] 
**currency** | **str** | The fiat currency for the off-ramp. | [optional] 
**order_amount** | **str** | This field has been deprecated. Please use &#x60;pricing_amount&#x60; instead. | [optional] 
**settlement_status** | [**SettleStatus**](SettleStatus.md) |  | [optional] 
**refund_id** | **str** | The refund order ID. | 
**amount** | **str** | The amount in cryptocurrency to be returned for this refund order. | 
**to_address** | **str** | The recipient&#39;s wallet address where the refund will be sent. | 
**refund_type** | [**RefundType**](RefundType.md) |  | [optional] 
**charge_merchant_fee** | **bool** | Whether to charge developer fee to the merchant for the refund.    - &#x60;true&#x60;: The fee amount (specified in &#x60;merchant_fee_amount&#x60;) will be deducted from the merchant&#39;s balance and added to the developer&#39;s balance    - &#x60;false&#x60;: The merchant is not charged any developer fee.  | [optional] 
**merchant_fee_amount** | **str** | The developer fee amount to charge the merchant, denominated in the cryptocurrency specified by &#x60;merchant_fee_token_id&#x60;. This is only applicable if &#x60;charge_merchant_fee&#x60; is set to &#x60;true&#x60;. | [optional] 
**merchant_fee_token_id** | **str** | The ID of the cryptocurrency used for the developer fee. This is only applicable if &#x60;charge_merchant_fee&#x60; is set to true. | [optional] 
**commission_fee** | [**CommissionFee**](CommissionFee.md) |  | [optional] 
**settlement_request_id** | **str** | The settlement request ID generated by Cobo. | 
**settlements** | [**List[SettlementDetail]**](SettlementDetail.md) |  | 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | 
**payout_channel** | [**PayoutChannel**](PayoutChannel.md) |  | 
**settlement_type** | [**SettlementType**](SettlementType.md) |  | [optional] 
**received_amount_fiat** | **str** | The estimated amount of the fiat currency to receive after off-ramping. This amount is subject to change due to bank transfer fees. | [optional] 
**bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**payer_id** | **str** | A unique identifier assigned by Cobo to track and identify individual payers. | 
**custom_payer_id** | **str** | A unique identifier assigned by the developer to track and identify individual payers in their system. | 
**chain** | **str** | The chain ID. | 
**previous_address** | **str** | The previous top-up address that was assigned to the payer. | 
**updated_address** | **str** | The new top-up address that has been assigned to the payer. | 
**payout_id** | **str** | The payout ID generated by Cobo. | 
**source_account** | **str** | The source account from which the bulk send will be made. - If the source account is a merchant account, provide the merchant&#39;s ID (e.g., \&quot;M1001\&quot;). - If the source account is the developer account, use the string &#x60;\&quot;developer\&quot;&#x60;.  | 
**payout_items** | [**List[PaymentPayoutItem]**](PaymentPayoutItem.md) | required | [optional] 
**recipient_info** | [**PaymentPayoutRecipientInfo**](PaymentPayoutRecipientInfo.md) |  | [optional] 
**actual_payout_amount** | **str** | - For &#x60;Crypto&#x60; payouts: The amount of cryptocurrency sent to the recipient&#39;s address, denominated in the token specified in &#x60;recipient_info.token_id&#x60;. - For &#x60;OffRamp&#x60; payouts: The amount of fiat currency sent to the recipient&#39;s bank account, denominated in the currency specified in &#x60;recipient_info.currency&#x60;. (Note: The actual amount received may be lower due to additional bank transfer fees.)  | [optional] 
**remark** | **str** | A note or comment about the payout. | [optional] 
**bulk_send_id** | **str** | The bulk send ID. | 
**execution_mode** | [**PaymentBulkSendExecutionMode**](PaymentBulkSendExecutionMode.md) |  | 
**disposition_type** | [**DispositionType**](DispositionType.md) |  | 
**disposition_status** | [**DispositionStatus**](DispositionStatus.md) |  | 
**destination_address** | **str** | The blockchain address to receive the refunded/isolated funds. | [optional] 
**disposition_amount** | **str** | The amount to be refunded/isolated from the original transaction, specified as a numeric string. This value cannot exceed the total amount of the original transaction.  | [optional] 
**transaction_type** | [**KytScreeningsTransactionType**](KytScreeningsTransactionType.md) |  | 
**review_status** | [**ReviewStatusType**](ReviewStatusType.md) |  | 
**funds_status** | [**FundsStatusType**](FundsStatusType.md) |  | 
**screening_id** | **str** | The unique system-generated identifier for this screening request (UUID format, fixed 36 characters). | 

## Example

```python
from cobo_waas2.models.webhook_event_data import WebhookEventData

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventData from a JSON string
webhook_event_data_instance = WebhookEventData.from_json(json)
# print the JSON string representation of the object
print(WebhookEventData.to_json())

# convert the object into a dict
webhook_event_data_dict = webhook_event_data_instance.to_dict()
# create an instance of WebhookEventData from a dict
webhook_event_data_from_dict = WebhookEventData.from_dict(webhook_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


