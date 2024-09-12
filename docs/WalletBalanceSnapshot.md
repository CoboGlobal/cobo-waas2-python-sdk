# WalletBalanceSnapshot

The snapshot information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **int** | The snapshot ID. | 
**snapshot_name** | **str** | The snapshot name. | [optional] 

## Example

```python
from cobo_waas2.models.wallet_balance_snapshot import WalletBalanceSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of WalletBalanceSnapshot from a JSON string
wallet_balance_snapshot_instance = WalletBalanceSnapshot.from_json(json)
# print the JSON string representation of the object
print(WalletBalanceSnapshot.to_json())

# convert the object into a dict
wallet_balance_snapshot_dict = wallet_balance_snapshot_instance.to_dict()
# create an instance of WalletBalanceSnapshot from a dict
wallet_balance_snapshot_from_dict = WalletBalanceSnapshot.from_dict(wallet_balance_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


