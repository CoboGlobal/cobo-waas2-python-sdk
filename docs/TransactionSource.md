# TransactionSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**signer_key_share_holder_group_id** | **str** | The ID of the key share holder group that is selected to sign the transaction. | [optional] 
**delegate** | [**CoboSafeDelegate**](CoboSafeDelegate.md) |  | [optional] 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | 
**trading_account_type** | **str** | The exchange trading account or a sub-wallet ID. | [optional] 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**addresses** | **List[str]** | A list of addresses. | 

## Example

```python
from cobo_waas2.models.transaction_source import TransactionSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSource from a JSON string
transaction_source_instance = TransactionSource.from_json(json)
# print the JSON string representation of the object
print(TransactionSource.to_json())

# convert the object into a dict
transaction_source_dict = transaction_source_instance.to_dict()
# create an instance of TransactionSource from a dict
transaction_source_from_dict = TransactionSource.from_dict(transaction_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


