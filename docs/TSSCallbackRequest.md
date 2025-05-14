# TSSCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | he unique ID of the callback request. | [optional] 
**request_type** | [**TSSCallbackRequestType**](TSSCallbackRequestType.md) |  | [optional] 
**request_detail** | **str** | Details specific to the request type. The structure varies depending on the request type.  The content is a JSON-serialized string. | [optional] 
**extra_info** | **str** | Additional contextual information.  The structure varies depending on the request type. The content is a JSON-serialized string. | [optional] 

## Example

```python
from cobo_waas2.models.tss_callback_request import TSSCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TSSCallbackRequest from a JSON string
tss_callback_request_instance = TSSCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(TSSCallbackRequest.to_json())

# convert the object into a dict
tss_callback_request_dict = tss_callback_request_instance.to_dict()
# create an instance of TSSCallbackRequest from a dict
tss_callback_request_from_dict = TSSCallbackRequest.from_dict(tss_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


