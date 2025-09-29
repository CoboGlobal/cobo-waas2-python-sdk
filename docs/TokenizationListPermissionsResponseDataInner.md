# TokenizationListPermissionsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address with permissions. | 
**permissions** | [**List[TokenizationTokenPermissionType]**](TokenizationTokenPermissionType.md) | The permissions assigned to this address. | 

## Example

```python
from cobo_waas2.models.tokenization_list_permissions_response_data_inner import TokenizationListPermissionsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationListPermissionsResponseDataInner from a JSON string
tokenization_list_permissions_response_data_inner_instance = TokenizationListPermissionsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(TokenizationListPermissionsResponseDataInner.to_json())

# convert the object into a dict
tokenization_list_permissions_response_data_inner_dict = tokenization_list_permissions_response_data_inner_instance.to_dict()
# create an instance of TokenizationListPermissionsResponseDataInner from a dict
tokenization_list_permissions_response_data_inner_from_dict = TokenizationListPermissionsResponseDataInner.from_dict(tokenization_list_permissions_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


