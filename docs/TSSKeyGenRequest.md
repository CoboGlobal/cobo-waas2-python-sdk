# TSSKeyGenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **int** | The number of key share holders required to approve each operation in TSS key share group. | [optional] 
**node_ids** | **List[str]** |  | [optional] 
**curve** | [**TSSCurve**](TSSCurve.md) |  | [optional] 
**task_id** | **str** | The task ID. | [optional] 
**biz_task_id** | **str** | The business task ID. This field contains the TSS request ID. | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_gen_request import TSSKeyGenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyGenRequest from a JSON string
tss_key_gen_request_instance = TSSKeyGenRequest.from_json(json)
# print the JSON string representation of the object
print(TSSKeyGenRequest.to_json())

# convert the object into a dict
tss_key_gen_request_dict = tss_key_gen_request_instance.to_dict()
# create an instance of TSSKeyGenRequest from a dict
tss_key_gen_request_from_dict = TSSKeyGenRequest.from_dict(tss_key_gen_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


