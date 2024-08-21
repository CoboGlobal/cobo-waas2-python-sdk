# GetToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token. | [optional] 
**token_type** | **str** | The type of the tokens, which is Bearer. | [optional] 
**scope** | **str** | The scope of the access token to limit the app&#39;s access to the organization&#39;s resources.  **Note**: Currently this property value is empty. The scope of the access token is based on the permissions granted when the app user installs the app.  | [optional] 
**expires_in** | **int** | The time in seconds in which the access token expires. | [optional] 
**refresh_token** | **str** | The refresh token, used to obtain a new access token when the current access token expires. | [optional] 

## Example

```python
from cobo_waas2.models.get_token200_response import GetToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetToken200Response from a JSON string
get_token200_response_instance = GetToken200Response.from_json(json)
# print the JSON string representation of the object
print(GetToken200Response.to_json())

# convert the object into a dict
get_token200_response_dict = get_token200_response_instance.to_dict()
# create an instance of GetToken200Response from a dict
get_token200_response_from_dict = GetToken200Response.from_dict(get_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


