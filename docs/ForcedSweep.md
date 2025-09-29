# ForcedSweep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forced_sweep_id** | **str** | The force sweep ID. | 
**request_id** | **str** | The request ID provided by you when creating the force sweep request. | 
**wallet_id** | **str** | The wallet ID to force sweep, which is the unique identifier of a wallet. | [optional] 
**token_id** | **str** | The token ID to force sweep, which is the unique identifier of a token. | [optional] 
**amount** | **str** | The amount of needing force sweep. | [optional] 
**status** | [**ForcedSweepStatus**](ForcedSweepStatus.md) |  | 
**created_timestamp** | **int** | The created time of the force sweep request, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The updated time of the force sweep request, represented as a UNIX timestamp in seconds. | [optional] 

## Example

```python
from cobo_waas2.models.forced_sweep import ForcedSweep

# TODO update the JSON string below
json = "{}"
# create an instance of ForcedSweep from a JSON string
forced_sweep_instance = ForcedSweep.from_json(json)
# print the JSON string representation of the object
print(ForcedSweep.to_json())

# convert the object into a dict
forced_sweep_dict = forced_sweep_instance.to_dict()
# create an instance of ForcedSweep from a dict
forced_sweep_from_dict = ForcedSweep.from_dict(forced_sweep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


