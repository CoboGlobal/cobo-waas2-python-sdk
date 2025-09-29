# ExchangePermissionToken201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The new Permission Access Token. | [optional] 
**token_type** | **str** | The type of the tokens, which is Bearer. | [optional] 
**expires_in** | **int** | The time in seconds in which the new Permission Access Token expires. | [optional] 
**refresh_token** | **str** | The Refresh Token, used to obtain another Org Access Token when the new Permission Access Token expires. The expiration time for Refresh Tokens is currently set to 7 days and is subject to change. | [optional] 

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


