# UpdateMpcVaultByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the vault. | 

## Example

```python
from cobo_waas2.models.update_mpc_vault_by_id_request import UpdateMpcVaultByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMpcVaultByIdRequest from a JSON string
update_mpc_vault_by_id_request_instance = UpdateMpcVaultByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMpcVaultByIdRequest.to_json())

# convert the object into a dict
update_mpc_vault_by_id_request_dict = update_mpc_vault_by_id_request_instance.to_dict()
# create an instance of UpdateMpcVaultByIdRequest from a dict
update_mpc_vault_by_id_request_from_dict = UpdateMpcVaultByIdRequest.from_dict(update_mpc_vault_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


