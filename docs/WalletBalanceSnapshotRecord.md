# WalletBalanceSnapshotRecord

The token snapshot detail information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | [optional] 
**wallet_name** | **str** | The wallet name. | [optional] 
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens). | 
**balance** | **str** | The balance of the token. | 

## Example

```python
from cobo_waas2.models.wallet_balance_snapshot_record import WalletBalanceSnapshotRecord

# TODO update the JSON string below
json = "{}"
# create an instance of WalletBalanceSnapshotRecord from a JSON string
wallet_balance_snapshot_record_instance = WalletBalanceSnapshotRecord.from_json(json)
# print the JSON string representation of the object
print(WalletBalanceSnapshotRecord.to_json())

# convert the object into a dict
wallet_balance_snapshot_record_dict = wallet_balance_snapshot_record_instance.to_dict()
# create an instance of WalletBalanceSnapshotRecord from a dict
wallet_balance_snapshot_record_from_dict = WalletBalanceSnapshotRecord.from_dict(wallet_balance_snapshot_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


