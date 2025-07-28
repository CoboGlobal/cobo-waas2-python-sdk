# ForcedSweepRequest

The information about the request to force sweep.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request id of the force sweep. | 
**wallet_id** | **str** | The wallet ID to force sweep, which is the unique identifier of a wallet. | 
**token_id** | **str** | The token ID to force sweep, which is the unique identifier of a token. | 
**amount** | **str** | The amount of needing force sweep. | 

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


