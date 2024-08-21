# SubWalletAssetBalance

The information about the asset balance of a trading account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_account_type** | **str** | The trading account type. | [optional] 
**asset_id** | **str** | The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | 
**balance** | [**TokenBalanceBalance**](TokenBalanceBalance.md) |  | 

## Example

```python
from cobo_waas2.models.sub_wallet_asset_balance import SubWalletAssetBalance

# TODO update the JSON string below
json = "{}"
# create an instance of SubWalletAssetBalance from a JSON string
sub_wallet_asset_balance_instance = SubWalletAssetBalance.from_json(json)
# print the JSON string representation of the object
print(SubWalletAssetBalance.to_json())

# convert the object into a dict
sub_wallet_asset_balance_dict = sub_wallet_asset_balance_instance.to_dict()
# create an instance of SubWalletAssetBalance from a dict
sub_wallet_asset_balance_from_dict = SubWalletAssetBalance.from_dict(sub_wallet_asset_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


