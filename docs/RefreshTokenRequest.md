# RefreshTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client ID, a unique identifier to distinguish Cobo Portal Apps. You can get the client ID by retrieving the manifest file after publishing the app. | [optional] 
**grant_type** | **str** | The OAuth grant type. Set the value as &#x60;refresh_token&#x60;. | [optional] 
**refresh_token** | **str** | The Refresh Token of the current Org Access Token. | [optional] 

## Example

```python
from cobo_waas2.models.refresh_token_request import RefreshTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenRequest from a JSON string
refresh_token_request_instance = RefreshTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenRequest.to_json())

# convert the object into a dict
refresh_token_request_dict = refresh_token_request_instance.to_dict()
# create an instance of RefreshTokenRequest from a dict
refresh_token_request_from_dict = RefreshTokenRequest.from_dict(refresh_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


