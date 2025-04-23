# WebhookEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  The data type of the event. - &#x60;Transaction&#x60;: The transaction event data. - &#x60;TSSRequest&#x60;: The TSS request event data. - &#x60;Addresses&#x60;: The addresses event data. - &#x60;WalletInfo&#x60;: The wallet information event data. - &#x60;MPCVault&#x60;: The MPC vault event data. - &#x60;Chains&#x60;: The enabled chain event data. - &#x60;Tokens&#x60;: The enabled token event data. - &#x60;TokenListing&#x60;: The token listing event data.        - &#x60;PaymentOrder&#x60;: The payment order event data. - &#x60;PaymentRefund&#x60;: The payment refund event data. - &#x60;PaymentSettlement&#x60;: The payment settlement event data. | 
**transaction_id** | **str** | The transaction ID. | 
**cobo_id** | **str** | The Cobo ID, which can be used to track a transaction. | [optional] 
**request_id** | **str** | The request ID provided by you when creating the settlement request. | 
**wallet_id** | **str** | For deposit transactions, this property represents the wallet ID of the transaction destination. For transactions of other types, this property represents the wallet ID of the transaction source. | 
**type** | [**MPCVaultType**](MPCVaultType.md) |  | [optional] 
**status** | [**SettleRequestStatus**](SettleRequestStatus.md) |  | 
**sub_status** | [**TransactionSubStatus**](TransactionSubStatus.md) |  | [optional] 
**failed_reason** | **str** | (This property is applicable to approval failures and signature failures only) The reason why the transaction failed. | [optional] 
**chain_id** | **str** | The ID of the blockchain network on which the refund transaction occurs. | 
**token_id** | **str** | The ID of the cryptocurrency used for refund. | 
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
**source** | [**TokenListingRequestSource**](TokenListingRequestSource.md) |  | 
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
**description** | **str** | The description of the TSS request. | [optional] 
**is_loop** | **bool** | Whether the transaction was executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer. - &#x60;true&#x60;: The transaction was executed as a Cobo Loop transfer. - &#x60;false&#x60;: The transaction was not executed as a Cobo Loop transfer.  | [optional] 
**cobo_category** | **List[str]** | The transaction category defined by Cobo. Possible values include:  - &#x60;AutoSweep&#x60;: An auto-sweep transaction. - &#x60;AutoFueling&#x60;: A transaction where Fee Station pays transaction fees to an address within your wallet. - &#x60;AutoFuelingRefund&#x60;: A refund for an auto-fueling transaction. - &#x60;SafeTxMessage&#x60;: A message signing transaction to authorize a Smart Contract Wallet (Safe\\{Wallet\\}) transaction. - &#x60;BillPayment&#x60;: A transaction to pay Cobo bills through Fee Station. - &#x60;BillRefund&#x60;: A refund for a previously made bill payment. - &#x60;CommissionFeeCharge&#x60;: A transaction to charge commission fees via Fee Station. - &#x60;CommissionFeeRefund&#x60;: A refund of previously charged commission fees.  | [optional] 
**extra** | **List[str]** | A list of JSON-encoded strings containing structured, business-specific extra information for the transaction. Each item corresponds to a specific data type, indicated by the &#x60;extra_type&#x60; field in the JSON object (for example, \&quot;BabylonBusinessInfo\&quot;, \&quot;BtcAddressInfo\&quot;).  | [optional] 
**fueling_info** | [**TransactionFuelingInfo**](TransactionFuelingInfo.md) |  | [optional] 
**created_timestamp** | **int** | Timestamp when the request was created (in milliseconds since Unix epoch) | 
**updated_timestamp** | **int** | Timestamp when the request was last updated (in milliseconds since Unix epoch) | 
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
**contract_address** | **str** | Contract address of the token | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**token** | [**TokenInfo**](TokenInfo.md) |  | [optional] 
**feedback** | **str** | Feedback provided by the admin for rejected requests | [optional] 
**order_id** | **str** | The order ID. | 
**merchant_id** | **str** | The merchant ID. | [optional] 
**payable_amount** | **str** | The cryptocurrency amount to be paid for this order. | 
**receive_address** | **str** | The recipient wallet address to be used for the payment transaction. | 
**currency** | **str** | The fiat currency of the order. | 
**order_amount** | **str** | The base amount of the order in fiat currency, excluding the developer fee (specified in &#x60;fee_amount&#x60;). | 
**fee_amount** | **str** | The developer fee for the order in fiat currency. It is added to the base amount (&#x60;order_amount&#x60;) to determine the final charge. | 
**exchange_rate** | **str** | The exchange rate between a currency pair. Expressed as the amount of fiat currency per one unit of cryptocurrency. For example, if the cryptocurrency is USDT and the fiat currency is USD, a rate of \&quot;0.99\&quot; means 1 USDT &#x3D; 0.99 USD. | 
**expired_at** | **int** | The expiration time of the pay-in order, represented as a UNIX timestamp in seconds. | [optional] 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by the developer to identify this order in their system. | 
**received_token_amount** | **str** | The total cryptocurrency amount received for this order. Updates until the expiration time. Precision matches the token standard (e.g., 6 decimals for USDT). | 
**refund_id** | **str** | The refund order ID. | 
**amount** | **str** | The amount in cryptocurrency to be returned for this refund order. | 
**to_address** | **str** | The recipient&#39;s wallet address where the refund will be sent. | 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of transactions associated with this refund order. Each transaction represents a separate blockchain operation related to the refund process. | [optional] 
**settlement_request_id** | **str** | The settlement request ID generated by Cobo. | 
**settlements** | [**List[SettlementDetail]**](SettlementDetail.md) |  | 

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


