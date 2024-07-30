# SafeTransferSource

The information about the transaction source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 
**delegate** | [**CoboSafeDelegate**](CoboSafeDelegate.md) |  | 

## Example

```python
from cobo_waas2.models.safe_transfer_source import SafeTransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of SafeTransferSource from a JSON string
safe_transfer_source_instance = SafeTransferSource.from_json(json)
# print the JSON string representation of the object
print(SafeTransferSource.to_json())

# convert the object into a dict
safe_transfer_source_dict = safe_transfer_source_instance.to_dict()
# create an instance of SafeTransferSource from a dict
safe_transfer_source_from_dict = SafeTransferSource.from_dict(safe_transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


