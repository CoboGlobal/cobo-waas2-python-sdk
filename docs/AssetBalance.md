# AssetBalance

The data for token balance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | 
**balance** | [**TokenBalanceBalance**](TokenBalanceBalance.md) |  | 

## Example

```python
from cobo_waas2.models.asset_balance import AssetBalance

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBalance from a JSON string
asset_balance_instance = AssetBalance.from_json(json)
# print the JSON string representation of the object
print(AssetBalance.to_json())

# convert the object into a dict
asset_balance_dict = asset_balance_instance.to_dict()
# create an instance of AssetBalance from a dict
asset_balance_from_dict = AssetBalance.from_dict(asset_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


