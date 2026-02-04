# SupportedToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The unique identifier of the token, in the format of &#x60;{chain_id}_{token_symbol}&#x60;. | 
**name** | **str** | The full name of the token. | 
**symbol** | **str** | The symbol of the token. | 
**decimal** | **int** | The number of decimal places for the token. This value is used to convert  between the token&#39;s smallest unit and its display value.  | 
**token_address** | **str** | The contract address of the token. This is &#x60;null&#x60; for native coins (e.g., ETH on Ethereum).  | 
**chain_id** | **str** | The ID of the chain on which the token exists. | 
**chain_symbol** | **str** | The symbol of the chain on which the token exists. | 
**chain_icon_url** | **str** | The URL of the chain icon image. | [optional] 
**token_icon_url** | **str** | The URL of the token icon image. | [optional] 
**can_off_ramp** | **bool** | Whether the token supports fiat off-ramp. - &#x60;true&#x60;: The token can be used for fiat off-ramp. - &#x60;false&#x60;: The token cannot be used for fiat off-ramp.  | [optional] 

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


