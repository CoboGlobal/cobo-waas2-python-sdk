# TransactionMPCWalletSource

Information about the transaction source type `Org-Controlled` and `User-Controlled`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | [optional] 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**signer_key_share_holder_group_id** | **str** | The ID of the key share holder group that is selected to sign the transaction. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_mpc_wallet_source import TransactionMPCWalletSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMPCWalletSource from a JSON string
transaction_mpc_wallet_source_instance = TransactionMPCWalletSource.from_json(json)
# print the JSON string representation of the object
print(TransactionMPCWalletSource.to_json())

# convert the object into a dict
transaction_mpc_wallet_source_dict = transaction_mpc_wallet_source_instance.to_dict()
# create an instance of TransactionMPCWalletSource from a dict
transaction_mpc_wallet_source_from_dict = TransactionMPCWalletSource.from_dict(transaction_mpc_wallet_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


