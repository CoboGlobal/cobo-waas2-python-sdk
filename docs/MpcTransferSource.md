# MpcTransferSource

The information about the transaction source types `Org-Controlled` and `User-Controlled`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  - For UTXO-based chains: both `address` and `included_utxos` are optional. If both `address` and `included_utxos` are provided, the UTXOs must belong to the specified address. If neither `address` nor `included_utxos` is provided, the system will select UTXOs from the wallet associated with `wallet_id`. - For account-based chains: You need to provide `address` otherwise the token transfer will fail. However, when estimating fees for a transfer, `address` is not required.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | Indicates the wallet address to be used as the source of funds. - For UTXO-based chains: both &#x60;address&#x60; and &#x60;included_utxos&#x60; are optional. If both &#x60;address&#x60; and &#x60;included_utxos&#x60; are provided, the UTXOs must belong to the specified address. If neither &#x60;address&#x60; nor &#x60;included_utxos&#x60; is provided, the system will select UTXOs from the wallet associated with &#x60;wallet_id&#x60;.   For RBF transactions, please note the following:     - If the original transaction did not specify &#x60;included_utxos&#x60;, the RBF transaction may omit &#x60;address&#x60;, &#x60;included_utxos&#x60;, or both.     - If the original transaction specified &#x60;included_utxos&#x60;, the RBF transaction must specify either &#x60;address&#x60; or &#x60;included_utxos&#x60;, or both.     - The &#x60;address&#x60; or &#x60;included_utxos&#x60; in the RBF transaction may differ from those in the original transaction.  - For account-based chains: You need to provide &#x60;address&#x60; otherwise the token transfer will fail. However, when estimating fees for a transfer, &#x60;address&#x60; is not required.  | [optional] 
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


