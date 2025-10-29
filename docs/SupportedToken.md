# SupportedToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | Unique identifier of the token | 
**name** | **str** | Full name of the token | 
**symbol** | **str** | Symbol representation of the token | 
**decimal** | **int** | Number of decimal places for the token | 
**token_address** | **str** | Contract address of the token (may be null for native coins) | 
**chain_id** | **str** | Identifier of the blockchain where the token exists | 
**chain_symbol** | **str** | Symbol of the underlying blockchain | 
**chain_icon_url** | **str** | URL to the blockchain&#39;s icon image | [optional] 
**token_icon_url** | **str** | URL to the token&#39;s icon image | [optional] 
**can_off_ramp** | **bool** | Whether the token is supported by the off-ramp service. | [optional] 

## Example

```python
from cobo_waas2.models.supported_token import SupportedToken

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedToken from a JSON string
supported_token_instance = SupportedToken.from_json(json)
# print the JSON string representation of the object
print(SupportedToken.to_json())

# convert the object into a dict
supported_token_dict = supported_token_instance.to_dict()
# create an instance of SupportedToken from a dict
supported_token_from_dict = SupportedToken.from_dict(supported_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


