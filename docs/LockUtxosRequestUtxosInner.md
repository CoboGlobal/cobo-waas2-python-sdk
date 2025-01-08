# LockUtxosRequestUtxosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**tx_hash** | **str** | The transaction hash. | 
**vout_n** | **int** | The output index of the UTXO. | 

## Example

```python
from cobo_waas2.models.lock_utxos_request_utxos_inner import LockUtxosRequestUtxosInner

# TODO update the JSON string below
json = "{}"
# create an instance of LockUtxosRequestUtxosInner from a JSON string
lock_utxos_request_utxos_inner_instance = LockUtxosRequestUtxosInner.from_json(json)
# print the JSON string representation of the object
print(LockUtxosRequestUtxosInner.to_json())

# convert the object into a dict
lock_utxos_request_utxos_inner_dict = lock_utxos_request_utxos_inner_instance.to_dict()
# create an instance of LockUtxosRequestUtxosInner from a dict
lock_utxos_request_utxos_inner_from_dict = LockUtxosRequestUtxosInner.from_dict(lock_utxos_request_utxos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


