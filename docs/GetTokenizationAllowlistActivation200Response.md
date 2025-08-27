# GetTokenizationAllowlistActivation200Response

The response schema for retrieving the allowlist activation status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated** | **bool** | Indicates whether the allowlist feature is activated for the token. | 

## Example

```python
from cobo_waas2.models.get_tokenization_allowlist_activation200_response import GetTokenizationAllowlistActivation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTokenizationAllowlistActivation200Response from a JSON string
get_tokenization_allowlist_activation200_response_instance = GetTokenizationAllowlistActivation200Response.from_json(json)
# print the JSON string representation of the object
print(GetTokenizationAllowlistActivation200Response.to_json())

# convert the object into a dict
get_tokenization_allowlist_activation200_response_dict = get_tokenization_allowlist_activation200_response_instance.to_dict()
# create an instance of GetTokenizationAllowlistActivation200Response from a dict
get_tokenization_allowlist_activation200_response_from_dict = GetTokenizationAllowlistActivation200Response.from_dict(get_tokenization_allowlist_activation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


