# MpcTransferSource

The information about the transaction source types `Org-Controlled` and `User-Controlled`. Refer to [Transaction sources and destinations](/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  If you specify both the `address` or `included_utxos` properties, the specified included UTXOs must belong to the address.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | [optional] 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.mpc_transfer_source import MpcTransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of MpcTransferSource from a JSON string
mpc_transfer_source_instance = MpcTransferSource.from_json(json)
# print the JSON string representation of the object
print(MpcTransferSource.to_json())

# convert the object into a dict
mpc_transfer_source_dict = mpc_transfer_source_instance.to_dict()
# create an instance of MpcTransferSource from a dict
mpc_transfer_source_from_dict = MpcTransferSource.from_dict(mpc_transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


