# TSSKeyReshareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_group_id** | **str** | The old TSS key share group ID. | [optional] 
**root_pub_key** | **str** | The The old TSS key share group&#39;s root extended public key. | [optional] 
**curve** | [**TSSCurve**](TSSCurve.md) |  | [optional] 
**used_node_ids** | **List[str]** |  | [optional] 
**old_threshold** | **int** | The number of key share holders required to approve each operation in the old TSS key share group. | [optional] 
**new_threshold** | **int** | The number of key share holders required to approve each operation in the new TSS key share group. | [optional] 
**new_node_ids** | **List[str]** |  | [optional] 
**task_id** | **str** | The task ID. | [optional] 
**biz_task_id** | **str** | The business task ID. This field contains the TSS request ID. | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_reshare_request import TSSKeyReshareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyReshareRequest from a JSON string
tss_key_reshare_request_instance = TSSKeyReshareRequest.from_json(json)
# print the JSON string representation of the object
print(TSSKeyReshareRequest.to_json())

# convert the object into a dict
tss_key_reshare_request_dict = tss_key_reshare_request_instance.to_dict()
# create an instance of TSSKeyReshareRequest from a dict
tss_key_reshare_request_from_dict = TSSKeyReshareRequest.from_dict(tss_key_reshare_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


