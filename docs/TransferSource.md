# TransferSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**mpc_used_key_share_holder_group** | [**MpcSigningGroup**](MpcSigningGroup.md) |  | [optional] 
**delegate** | [**CoboSafeDelegate**](CoboSafeDelegate.md) |  | 
**trading_account_type** | **str** | The trading account type. | 

## Example

```python
from cobo_waas2.models.transfer_source import TransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransferSource from a JSON string
transfer_source_instance = TransferSource.from_json(json)
# print the JSON string representation of the object
print(TransferSource.to_json())

# convert the object into a dict
transfer_source_dict = transfer_source_instance.to_dict()
# create an instance of TransferSource from a dict
transfer_source_from_dict = TransferSource.from_dict(transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


