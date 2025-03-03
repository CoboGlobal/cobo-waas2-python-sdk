# TransactionRbfSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. If you want to specify the UTXOs to be used, please provide the &#x60;included_utxos&#x60; property. If you specify both the &#x60;address&#x60; and &#x60;included_utxos&#x60; properties, the specified included UTXOs must belong to the address. It is recommended to specify no more than 100 included UTXOs to ensure optimal transaction processing.  You need to provide either the &#x60;address&#x60; or &#x60;included_utxos&#x60; property. If neither property is provided, the transfer will fail.  | [optional] 
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


