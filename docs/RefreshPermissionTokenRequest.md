# RefreshPermissionTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | The Refresh Token of the current Access Token. | 

## Example

```python
from cobo_waas2.models.refresh_permission_token_request import RefreshPermissionTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshPermissionTokenRequest from a JSON string
refresh_permission_token_request_instance = RefreshPermissionTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RefreshPermissionTokenRequest.to_json())

# convert the object into a dict
refresh_permission_token_request_dict = refresh_permission_token_request_instance.to_dict()
# create an instance of RefreshPermissionTokenRequest from a dict
refresh_permission_token_request_from_dict = RefreshPermissionTokenRequest.from_dict(refresh_permission_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


