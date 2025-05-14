# TSSParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The node ID. | [optional] 
**share_id** | **str** | The share ID. | [optional] 
**share_public_key** | **str** | The share public key. | [optional] 

## Example

```python
from cobo_waas2.models.tss_participant import TSSParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of TSSParticipant from a JSON string
tss_participant_instance = TSSParticipant.from_json(json)
# print the JSON string representation of the object
print(TSSParticipant.to_json())

# convert the object into a dict
tss_participant_dict = tss_participant_instance.to_dict()
# create an instance of TSSParticipant from a dict
tss_participant_from_dict = TSSParticipant.from_dict(tss_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


