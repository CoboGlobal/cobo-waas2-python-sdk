# TokenizationUpdatePermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**action** | [**TokenizationPermissionAction**](TokenizationPermissionAction.md) |  | 
**address** | **str** | The address to manage permissions for. | 
**permissions** | [**List[TokenizationTokenPermissionType]**](TokenizationTokenPermissionType.md) | The list of permissions to operate on. | 
**app_initiator** | **str** | The initiator of the tokenization activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_update_permissions_request import TokenizationUpdatePermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdatePermissionsRequest from a JSON string
tokenization_update_permissions_request_instance = TokenizationUpdatePermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdatePermissionsRequest.to_json())

# convert the object into a dict
tokenization_update_permissions_request_dict = tokenization_update_permissions_request_instance.to_dict()
# create an instance of TokenizationUpdatePermissionsRequest from a dict
tokenization_update_permissions_request_from_dict = TokenizationUpdatePermissionsRequest.from_dict(tokenization_update_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


