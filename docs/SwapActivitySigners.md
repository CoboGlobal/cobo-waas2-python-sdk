# SwapActivitySigners

The signer information of the swap activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer** | **str** | The signer name. | [optional] 
**status** | [**SwapSingingStatus**](SwapSingingStatus.md) |  | [optional] 
**failed_reason** | **str** | The reason for the signing failure. | [optional] 

## Example

```python
from cobo_waas2.models.swap_activity_signers import SwapActivitySigners

# TODO update the JSON string below
json = "{}"
# create an instance of SwapActivitySigners from a JSON string
swap_activity_signers_instance = SwapActivitySigners.from_json(json)
# print the JSON string representation of the object
print(SwapActivitySigners.to_json())

# convert the object into a dict
swap_activity_signers_dict = swap_activity_signers_instance.to_dict()
# create an instance of SwapActivitySigners from a dict
swap_activity_signers_from_dict = SwapActivitySigners.from_dict(swap_activity_signers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


