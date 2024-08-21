# MPCWalletInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**name** | **str** | The wallet name. | 
**org_id** | **str** | The ID of the owning organization. | 
**project_id** | **str** | The project ID. | [optional] 
**project_name** | **str** | The project name. | [optional] 
**vault_id** | **str** | The ID of the owning vault. | 
**vault_name** | **str** | The vault name. | [optional] 

## Example

```python
from cobo_waas2.models.mpc_wallet_info import MPCWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MPCWalletInfo from a JSON string
mpc_wallet_info_instance = MPCWalletInfo.from_json(json)
# print the JSON string representation of the object
print(MPCWalletInfo.to_json())

# convert the object into a dict
mpc_wallet_info_dict = mpc_wallet_info_instance.to_dict()
# create an instance of MPCWalletInfo from a dict
mpc_wallet_info_from_dict = MPCWalletInfo.from_dict(mpc_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


