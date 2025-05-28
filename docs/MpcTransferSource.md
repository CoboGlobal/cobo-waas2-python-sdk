# MpcTransferSource

The information about the transaction source types `Org-Controlled` and `User-Controlled`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  You need to provide either the `address` or `included_utxos` property. If neither property is provided, the transfer will fail.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. If you want to specify the UTXOs to be used, please provide the &#x60;included_utxos&#x60; property. When &#x60;included_utxos&#x60; is specified, only these specified UTXOs will be used for the transaction. If you specify both the &#x60;address&#x60; and &#x60;included_utxos&#x60; properties, the specified included UTXOs must belong to the address. It is recommended to specify no more than 100 included UTXOs to ensure optimal transaction processing.  You need to provide either the &#x60;address&#x60; or &#x60;included_utxos&#x60; property. If neither property is provided, the transfer will fail.  | [optional] 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**mpc_used_key_share_holder_group** | [**MpcSigningGroup**](MpcSigningGroup.md) |  | [optional] 

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


