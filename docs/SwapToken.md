# SwapToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token id. | 
**chain_id** | **str** | The chain id. | 
**asset_id** | **str** | The asset id. | 
**token_address** | **str** | The token address. | [optional] 
**min_amount** | **str** | The minimum amount. | [optional] 
**max_amount** | **str** | The maximum amount. | [optional] 

## Example

```python
from cobo_waas2.models.swap_token import SwapToken

# TODO update the JSON string below
json = "{}"
# create an instance of SwapToken from a JSON string
swap_token_instance = SwapToken.from_json(json)
# print the JSON string representation of the object
print(SwapToken.to_json())

# convert the object into a dict
swap_token_dict = swap_token_instance.to_dict()
# create an instance of SwapToken from a dict
swap_token_from_dict = SwapToken.from_dict(swap_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


