# UpdateMpcWalletParams

The information of MPC Wallets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**name** | **str** | The wallet name. | 

## Example

```python
from cobo_waas2.models.update_mpc_wallet_params import UpdateMpcWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMpcWalletParams from a JSON string
update_mpc_wallet_params_instance = UpdateMpcWalletParams.from_json(json)
# print the JSON string representation of the object
print(UpdateMpcWalletParams.to_json())

# convert the object into a dict
update_mpc_wallet_params_dict = update_mpc_wallet_params_instance.to_dict()
# create an instance of UpdateMpcWalletParams from a dict
update_mpc_wallet_params_from_dict = UpdateMpcWalletParams.from_dict(update_mpc_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


