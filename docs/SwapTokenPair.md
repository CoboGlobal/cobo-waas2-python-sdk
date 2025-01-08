# SwapTokenPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_token_id** | **str** | The source token symbol. | [optional] 
**receive_token_id** | **str** | The target token symbol. | [optional] 

## Example

```python
from cobo_waas2.models.swap_token_pair import SwapTokenPair

# TODO update the JSON string below
json = "{}"
# create an instance of SwapTokenPair from a JSON string
swap_token_pair_instance = SwapTokenPair.from_json(json)
# print the JSON string representation of the object
print(SwapTokenPair.to_json())

# convert the object into a dict
swap_token_pair_dict = swap_token_pair_instance.to_dict()
# create an instance of SwapTokenPair from a dict
swap_token_pair_from_dict = SwapTokenPair.from_dict(swap_token_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


