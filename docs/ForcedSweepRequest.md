# ForcedSweepRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a forced sweep. The request ID is provided by you and must be unique. | 
**wallet_id** | **str** | The ID of the wallet in which the funds will be forcefully swept. | 
**token_id** | **str** | The ID of the token to be forcefully swept. | 
**amount** | **str** | The amount of the token to be forcefully swept. | 

## Example

```python
from cobo_waas2.models.forced_sweep_request import ForcedSweepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForcedSweepRequest from a JSON string
forced_sweep_request_instance = ForcedSweepRequest.from_json(json)
# print the JSON string representation of the object
print(ForcedSweepRequest.to_json())

# convert the object into a dict
forced_sweep_request_dict = forced_sweep_request_instance.to_dict()
# create an instance of ForcedSweepRequest from a dict
forced_sweep_request_from_dict = ForcedSweepRequest.from_dict(forced_sweep_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


