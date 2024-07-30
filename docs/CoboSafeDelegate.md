# CoboSafeDelegate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegate_type** | [**CoboSafeDelegateType**](CoboSafeDelegateType.md) |  | 
**wallet_id** | **str** | The wallet ID of the Delegate. This is required when initiating a transfer from Smart Contract Wallets (Safe{Wallet}). | 
**address** | **str** | The wallet address of the Delegate. This is required when initiating a transfer from Smart Contract Wallets (Safe{Wallet}). | 

## Example

```python
from cobo_waas2.models.cobo_safe_delegate import CoboSafeDelegate

# TODO update the JSON string below
json = "{}"
# create an instance of CoboSafeDelegate from a JSON string
cobo_safe_delegate_instance = CoboSafeDelegate.from_json(json)
# print the JSON string representation of the object
print(CoboSafeDelegate.to_json())

# convert the object into a dict
cobo_safe_delegate_dict = cobo_safe_delegate_instance.to_dict()
# create an instance of CoboSafeDelegate from a dict
cobo_safe_delegate_from_dict = CoboSafeDelegate.from_dict(cobo_safe_delegate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


