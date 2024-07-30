# AssetInfo

The asset information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | 
**display_code** | **str** | The asset symbol. You can use the value for display purposes. | [optional] 
**description** | **str** | The description of the asset. | [optional] 
**icon_url** | **str** | The URL of the asset icon. | [optional] 

## Example

```python
from cobo_waas2.models.asset_info import AssetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AssetInfo from a JSON string
asset_info_instance = AssetInfo.from_json(json)
# print the JSON string representation of the object
print(AssetInfo.to_json())

# convert the object into a dict
asset_info_dict = asset_info_instance.to_dict()
# create an instance of AssetInfo from a dict
asset_info_from_dict = AssetInfo.from_dict(asset_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


