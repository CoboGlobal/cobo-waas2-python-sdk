# ReconLedgerEntry

The reconciliation ledger entry, representing an address's running balance after a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID (the Cobo transaction ID you provided in &#x60;transaction_ids&#x60;). | 
**block_time** | **int** | The time when the block containing the transaction was created, in Unix timestamp format, measured in milliseconds. | [optional] 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address involved in this entry. | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. | 
**amount** | **str** | The transaction amount for this entry, expressed in the token&#39;s main unit (already divided by the token&#39;s decimals). The value is signed - positive for deposits and negative for withdrawals. | 
**balance_after** | **str** | The running balance of the address for this token after this transaction, expressed in the token&#39;s main unit. | 
**transaction_hash** | **str** | The transaction hash on the blockchain. | [optional] 
**block_number** | **int** | The number of the block containing the transaction. | [optional] 

## Example

```python
from cobo_waas2.models.recon_ledger_entry import ReconLedgerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ReconLedgerEntry from a JSON string
recon_ledger_entry_instance = ReconLedgerEntry.from_json(json)
# print the JSON string representation of the object
print(ReconLedgerEntry.to_json())

# convert the object into a dict
recon_ledger_entry_dict = recon_ledger_entry_instance.to_dict()
# create an instance of ReconLedgerEntry from a dict
recon_ledger_entry_from_dict = ReconLedgerEntry.from_dict(recon_ledger_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


