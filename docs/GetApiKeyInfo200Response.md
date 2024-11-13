# GetApiKeyInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The API key name. | 
**curve_type** | **str** | The curve type used for the API key, which determines the cryptographic algorithm for key generation and signing. Possible values include: - &#x60;ED25519&#x60;: Ed25519 - &#x60;SECP256K1&#x60;: Secp256k1  | 
**key** | **str** | The API key value. | 
**callback_url** | **str** | The URL of the callback endpoint that receives callback messages triggered by this API key. | [optional] 
**valid_ips** | **List[str]** | (Applicable to permanent API keys only) The list of IP addresses that are allowed to use this API key. | [optional] 
**created_timestamp** | **int** | The time when the API key was registered, in Unix timestamp format, measured in milliseconds. | 
**updated_timestamp** | **int** | The time when the API key information was last updated, in Unix timestamp format, measured in milliseconds. | 
**expired_timestamp** | **int** | The time when the API key expires, in Unix timestamp format, measured in milliseconds. For permanent API keys, this property value is &#x60;null&#x60;. | [optional] 
**role_scopes** | [**List[RoleScopes]**](RoleScopes.md) | The list of user roles and wallet scopes associated with the API key. | [optional] 

## Example

```python
from cobo_waas2.models.get_api_key_info200_response import GetApiKeyInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiKeyInfo200Response from a JSON string
get_api_key_info200_response_instance = GetApiKeyInfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetApiKeyInfo200Response.to_json())

# convert the object into a dict
get_api_key_info200_response_dict = get_api_key_info200_response_instance.to_dict()
# create an instance of GetApiKeyInfo200Response from a dict
get_api_key_info200_response_from_dict = GetApiKeyInfo200Response.from_dict(get_api_key_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


