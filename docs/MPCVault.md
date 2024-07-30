# MPCVault

The data for vault information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_id** | **str** | The vault ID. | [optional] 
**project_id** | **str** | The project ID. | [optional] 
**name** | **str** | The vault name. | [optional] 
**type** | [**MPCVaultType**](MPCVaultType.md) |  | [optional] 
**root_pubkeys** | [**List[RootPubkey]**](RootPubkey.md) |  | [optional] 
**create_timestamp** | **int** | The vault&#39;s creation time in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.mpc_vault import MPCVault

# TODO update the JSON string below
json = "{}"
# create an instance of MPCVault from a JSON string
mpc_vault_instance = MPCVault.from_json(json)
# print the JSON string representation of the object
print(MPCVault.to_json())

# convert the object into a dict
mpc_vault_dict = mpc_vault_instance.to_dict()
# create an instance of MPCVault from a dict
mpc_vault_from_dict = MPCVault.from_dict(mpc_vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


