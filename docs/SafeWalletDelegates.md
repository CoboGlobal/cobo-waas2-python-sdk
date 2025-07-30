# SafeWalletDelegates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_type** | [**EstimateFeeRequestType**](EstimateFeeRequestType.md) |  | 
**address** | **str** | The address of the recipient. | [optional] 
**value** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 
**calldata** | **str** | The data used to invoke a specific function or method within the specified contract at the destination address, with a maximum length of 65,000 characters.  | [optional] 
**token_id** | **str** | The token ID. | 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;. | [optional] 

## Example

```python
from cobo_waas2.models.safe_wallet_delegates import SafeWalletDelegates

# TODO update the JSON string below
json = "{}"
# create an instance of SafeWalletDelegates from a JSON string
safe_wallet_delegates_instance = SafeWalletDelegates.from_json(json)
# print the JSON string representation of the object
print(SafeWalletDelegates.to_json())

# convert the object into a dict
safe_wallet_delegates_dict = safe_wallet_delegates_instance.to_dict()
# create an instance of SafeWalletDelegates from a dict
safe_wallet_delegates_from_dict = SafeWalletDelegates.from_dict(safe_wallet_delegates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


