# GetToken4XXResponse

The response of a failed request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The error name. | 
**error_message** | **str** | The error description. | [optional] 

## Example

```python
from cobo_waas2.models.get_token4_xx_response import GetToken4XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetToken4XXResponse from a JSON string
get_token4_xx_response_instance = GetToken4XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetToken4XXResponse.to_json())

# convert the object into a dict
get_token4_xx_response_dict = get_token4_xx_response_instance.to_dict()
# create an instance of GetToken4XXResponse from a dict
get_token4_xx_response_from_dict = GetToken4XXResponse.from_dict(get_token4_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


