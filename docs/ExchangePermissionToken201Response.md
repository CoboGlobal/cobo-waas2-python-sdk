# ExchangePermissionToken201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The Access Token. | [optional] 
**token_type** | **str** | The token type. This is always &#x60;Bearer&#x60;. | [optional] 
**expires_in** | **int** | The time in seconds until the Access Token expires. This is always &#x60;3600&#x60;, indicating the token expires 1 hour after issuance. | [optional] 
**refresh_token** | **str** | The Refresh Token. Use it to obtain a new Access Token when the current one expires. The Refresh Token is valid for 7 days. | [optional] 

## Example

```python
from cobo_waas2.models.exchange_permission_token201_response import ExchangePermissionToken201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangePermissionToken201Response from a JSON string
exchange_permission_token201_response_instance = ExchangePermissionToken201Response.from_json(json)
# print the JSON string representation of the object
print(ExchangePermissionToken201Response.to_json())

# convert the object into a dict
exchange_permission_token201_response_dict = exchange_permission_token201_response_instance.to_dict()
# create an instance of ExchangePermissionToken201Response from a dict
exchange_permission_token201_response_from_dict = ExchangePermissionToken201Response.from_dict(exchange_permission_token201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


