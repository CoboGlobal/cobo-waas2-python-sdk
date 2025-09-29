# TokenizationUpdatePermissionsEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**action** | [**TokenizationPermissionAction**](TokenizationPermissionAction.md) |  | 
**address** | **str** | The address to manage permissions for. | 
**permissions** | [**List[TokenizationTokenPermissionType]**](TokenizationTokenPermissionType.md) | The list of permissions to operate on. | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**token_id** | **str** | The ID of the token. | 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_update_permissions_estimate_fee_params import TokenizationUpdatePermissionsEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdatePermissionsEstimateFeeParams from a JSON string
tokenization_update_permissions_estimate_fee_params_instance = TokenizationUpdatePermissionsEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdatePermissionsEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_update_permissions_estimate_fee_params_dict = tokenization_update_permissions_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationUpdatePermissionsEstimateFeeParams from a dict
tokenization_update_permissions_estimate_fee_params_from_dict = TokenizationUpdatePermissionsEstimateFeeParams.from_dict(tokenization_update_permissions_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


