# TransactionDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**account_output** | [**TransactionTransferToAddressDestinationAccountOutput**](TransactionTransferToAddressDestinationAccountOutput.md) |  | [optional] 
**utxo_outputs** | [**List[TransactionTransferToAddressDestinationUtxoOutputsInner]**](TransactionTransferToAddressDestinationUtxoOutputsInner.md) |  | [optional] 
**change_address** | **str** | The address used to receive the remaining funds or change from the transaction. | [optional] 
**force_internal** | **bool** | Whether the transaction request must be executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer.   - &#x60;true&#x60;: The transaction request must be executed as a Cobo Loop transfer.   - &#x60;false&#x60;: The transaction request may not be executed as a Cobo Loop transfer.  If both &#x60;force_internal&#x60; and &#x60;force_external&#x60; are set to &#x60;false&#x60;, the system uses Cobo Loop by default if possible; otherwise, it proceeds with an on-chain transfer.  | [optional] 
**force_external** | **bool** | Whether the transaction request must not be executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer.   - &#x60;true&#x60;: The transaction request must not be executed as a Cobo Loop transfer.   - &#x60;false&#x60;: The transaction request can be executed as a Cobo Loop transfer.  If both &#x60;force_internal&#x60; and &#x60;force_external&#x60; are set to &#x60;false&#x60;, the system uses Cobo Loop by default if possible; otherwise, it proceeds with an on-chain transfer.  | [optional] 
**wallet_id** | **str** | The wallet ID. | 
**trading_account_type** | **str** | The trading account type. | [optional] 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | [optional] 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | 
**address** | **str** | The destination address. | 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 
**calldata** | **str** | The data used to invoke a specific function or method within the specified contract at the destination address, with a maximum length of 65,000 characters.  | 
**calldata_info** | [**TransactionEvmCalldataInfo**](TransactionEvmCalldataInfo.md) |  | [optional] 
**instructions** | [**List[TransactionSolContractInstruction]**](TransactionSolContractInstruction.md) |  | [optional] 
**cosmos_messages** | [**List[TransactionCosmosMessage]**](TransactionCosmosMessage.md) |  | 
**message** | **str** | The raw data of the message to be signed, encoded in Base64 format. | 
**raw_structured_data** | **str** | The raw structured data to be signed, formatted as a JSON string. | [optional] 
**structured_data** | **Dict[str, object]** | The structured data to be signed, formatted as a JSON object according to the EIP-712 standard. | 
**safe_tx_extra_data** | [**SafeTxExtraData**](SafeTxExtraData.md) |  | [optional] 
**msg_hash** | **str** | Message hash to be signed, in hexadecimal format. | [optional] 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**memo** | **str** | The memo that identifies a transaction in order to credit the correct account. For transfers out of Cobo Portal, it is highly recommended to include a memo for the chains such as XRP, EOS, XLM, IOST, BNB_BNB, ATOM, LUNA, and TON. | [optional] 
**tx_info** | [**TransactionDepositToAddressDestinationTxInfo**](TransactionDepositToAddressDestinationTxInfo.md) |  | [optional] 
**message_bip137** | **str** | Message to be signed, in hexadecimal format. | 
**message_bip322** | **str** | Message to be signed, in hexadecimal format. | 
**message_cosmos_adr36** | **str** | Message to be signed, in hexadecimal format. | 

## Example

```python
from cobo_waas2.models.transaction_destination import TransactionDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDestination from a JSON string
transaction_destination_instance = TransactionDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionDestination.to_json())

# convert the object into a dict
transaction_destination_dict = transaction_destination_instance.to_dict()
# create an instance of TransactionDestination from a dict
transaction_destination_from_dict = TransactionDestination.from_dict(transaction_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


