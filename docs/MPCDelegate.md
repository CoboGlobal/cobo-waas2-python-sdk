# MPCDelegate

The information about the MPC Wallet as the Delegate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegate_type** | [**CoboSafeDelegateType**](CoboSafeDelegateType.md) |  | 
**wallet_id** | **str** | The wallet ID of the Delegate. This is required when initiating a transfer or contract call from Smart Contract Wallets (Safe{Wallet}). | 
**address** | **str** | The wallet address of the Delegate. This is required when initiating a transfer or contract call from Smart Contract Wallets (Safe{Wallet}). | 

## Example

```python
from cobo_waas2.models.mpc_delegate import MPCDelegate

# TODO update the JSON string below
json = "{}"
# create an instance of MPCDelegate from a JSON string
mpc_delegate_instance = MPCDelegate.from_json(json)
# print the JSON string representation of the object
print(MPCDelegate.to_json())

# convert the object into a dict
mpc_delegate_dict = mpc_delegate_instance.to_dict()
# create an instance of MPCDelegate from a dict
mpc_delegate_from_dict = MPCDelegate.from_dict(mpc_delegate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


