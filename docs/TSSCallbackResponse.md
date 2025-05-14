# TSSCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The unique ID of the callback request. | [optional] 
**status** | **int** | The response status code. 0 indicates success.  Any other value indicates that an error occurred while processing the request in the callback server. | [optional] 
**action** | [**TSSCallbackActionType**](TSSCallbackActionType.md) |  | [optional] 
**error** | **str** | The error message. - When status is not 0, Contains internal error messages from the callback server. - When status is 0 and action is REJECT, Contains the specific reason for the rejection. | [optional] 

## Example

```python
from cobo_waas2.models.tss_callback_response import TSSCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TSSCallbackResponse from a JSON string
tss_callback_response_instance = TSSCallbackResponse.from_json(json)
# print the JSON string representation of the object
print(TSSCallbackResponse.to_json())

# convert the object into a dict
tss_callback_response_dict = tss_callback_response_instance.to_dict()
# create an instance of TSSCallbackResponse from a dict
tss_callback_response_from_dict = TSSCallbackResponse.from_dict(tss_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


