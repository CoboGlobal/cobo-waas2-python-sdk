# TransactionRbfSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | Indicates the wallet address to be used as the source of funds. - For UTXO-based chains: both &#x60;address&#x60; and &#x60;included_utxos&#x60; are optional. If both &#x60;address&#x60; and &#x60;included_utxos&#x60; are provided, the UTXOs must belong to the specified address. If neither &#x60;address&#x60; nor &#x60;included_utxos&#x60; is provided, the system will select UTXOs from the wallet associated with &#x60;wallet_id&#x60;. - For account-based chains: You need to provide &#x60;address&#x60; otherwise the token transfer will fail. However, when estimating fees for a transfer, &#x60;address&#x60; is not required.  For detailed rules on &#x60;address&#x60; and &#x60;included_utxos&#x60; in both regular and RBF transactions, see [Address and included_utxos usage](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations#address-and-included-utxos-usage).  | [optional] 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**mpc_used_key_share_holder_group** | [**MpcSigningGroup**](MpcSigningGroup.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_rbf_source import TransactionRbfSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRbfSource from a JSON string
transaction_rbf_source_instance = TransactionRbfSource.from_json(json)
# print the JSON string representation of the object
print(TransactionRbfSource.to_json())

# convert the object into a dict
transaction_rbf_source_dict = transaction_rbf_source_instance.to_dict()
# create an instance of TransactionRbfSource from a dict
transaction_rbf_source_from_dict = TransactionRbfSource.from_dict(transaction_rbf_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


