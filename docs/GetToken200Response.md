# GetToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token, used by Cobo Portal Apps to access specific resources of other organizations. | [optional] 
**token_type** | **str** | The type of the tokens. | [optional] 
**scope** | **str** | The scope of the access token. This property value is empty by design. | [optional] 
**expires_in** | **int** | The time in seconds in which the access token expires. | [optional] 
**refresh_token** | **str** | The refresh token, used by Cobo Portal Apps to obtain new access tokens when the access token expires. | [optional] 

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


