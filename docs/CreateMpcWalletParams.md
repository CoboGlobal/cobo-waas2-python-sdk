# CreateMpcWalletParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The wallet name. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**enable_auto_sweep** | **bool** | Enable the auto sweep feature for the wallet. This parameter only applies to MPC and Web3 wallets. | [optional] 
**vault_id** | **str** | The ID of the owning vault. You can call [List all vaults](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/list-all-vaults) to retrieve all vault IDs under your organization. | 

## Example

```python
from cobo_waas2.models.create_mpc_wallet_params import CreateMpcWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMpcWalletParams from a JSON string
create_mpc_wallet_params_instance = CreateMpcWalletParams.from_json(json)
# print the JSON string representation of the object
print(CreateMpcWalletParams.to_json())

# convert the object into a dict
create_mpc_wallet_params_dict = create_mpc_wallet_params_instance.to_dict()
# create an instance of CreateMpcWalletParams from a dict
create_mpc_wallet_params_from_dict = CreateMpcWalletParams.from_dict(create_mpc_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


