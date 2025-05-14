# TSSGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The TSS key share group ID. | [optional] 
**canonical_group_id** | **str** | The canonical group ID. | [optional] 
**protocol_group_id** | **str** | The protocol group ID. | [optional] 
**protocol_type** | **str** | The protocol type. | [optional] 
**created_timestamp** | **int** | The group creation timestamp, in Unix timestamp format, measured in milliseconds. | [optional] 
**type** | [**TSSGroupType**](TSSGroupType.md) |  | [optional] 
**root_extended_public_key** | **str** | The root extended public key. | [optional] 
**chaincode** | **str** | The chaincode. | [optional] 
**curve** | [**TSSCurveType**](TSSCurveType.md) |  | [optional] 
**threshold** | **int** | The threshold. | [optional] 
**participants** | [**List[TSSParticipant]**](TSSParticipant.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_group import TSSGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TSSGroup from a JSON string
tss_group_instance = TSSGroup.from_json(json)
# print the JSON string representation of the object
print(TSSGroup.to_json())

# convert the object into a dict
tss_group_dict = tss_group_instance.to_dict()
# create an instance of TSSGroup from a dict
tss_group_from_dict = TSSGroup.from_dict(tss_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


