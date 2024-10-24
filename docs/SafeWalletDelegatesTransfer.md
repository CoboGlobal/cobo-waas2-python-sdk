# SafeWalletDelegatesTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | [**EstimateFeeRequestType**](EstimateFeeRequestType.md) |  | 
**token_id** | **str** | The token ID. | 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;. | [optional] 
**address** | **str** | The address of the recipient. | [optional] 

## Example

```python
from cobo_waas2.models.safe_wallet_delegates_transfer import SafeWalletDelegatesTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of SafeWalletDelegatesTransfer from a JSON string
safe_wallet_delegates_transfer_instance = SafeWalletDelegatesTransfer.from_json(json)
# print the JSON string representation of the object
print(SafeWalletDelegatesTransfer.to_json())

# convert the object into a dict
safe_wallet_delegates_transfer_dict = safe_wallet_delegates_transfer_instance.to_dict()
# create an instance of SafeWalletDelegatesTransfer from a dict
safe_wallet_delegates_transfer_from_dict = SafeWalletDelegatesTransfer.from_dict(safe_wallet_delegates_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


