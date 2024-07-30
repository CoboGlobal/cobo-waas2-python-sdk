# CreateMpcVaultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID, which you can retrieve by calling [List all projects](/v2/api-references/wallets--mpc-wallets/list-all-projects).  **Notes:** 1. If you set &#x60;vault_type&#x60; to &#x60;OrgControlled&#x60;, the value of &#x60;project_id&#x60; will be ignored. 2. If you set &#x60;vault_type&#x60; to &#x60;UserControlled&#x60;, then &#x60;project_id&#x60; is required.  | [optional] 
**name** | **str** | The vault name. | 
**vault_type** | [**MPCVaultType**](MPCVaultType.md) |  | 

## Example

```python
from cobo_waas2.models.create_mpc_vault_request import CreateMpcVaultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMpcVaultRequest from a JSON string
create_mpc_vault_request_instance = CreateMpcVaultRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMpcVaultRequest.to_json())

# convert the object into a dict
create_mpc_vault_request_dict = create_mpc_vault_request_instance.to_dict()
# create an instance of CreateMpcVaultRequest from a dict
create_mpc_vault_request_from_dict = CreateMpcVaultRequest.from_dict(create_mpc_vault_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


