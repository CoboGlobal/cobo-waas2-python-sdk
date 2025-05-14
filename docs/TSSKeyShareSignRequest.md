# TSSKeyShareSignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The node ID of the key share holder. | [optional] 
**task_id** | **str** | The task ID. | [optional] 
**details** | [**List[TSSKeyShareSignDetail]**](TSSKeyShareSignDetail.md) |  | [optional] 
**biz_task_id** | **str** | The business task ID. This field contains the key share sign request ID. | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_share_sign_request import TSSKeyShareSignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyShareSignRequest from a JSON string
tss_key_share_sign_request_instance = TSSKeyShareSignRequest.from_json(json)
# print the JSON string representation of the object
print(TSSKeyShareSignRequest.to_json())

# convert the object into a dict
tss_key_share_sign_request_dict = tss_key_share_sign_request_instance.to_dict()
# create an instance of TSSKeyShareSignRequest from a dict
tss_key_share_sign_request_from_dict = TSSKeyShareSignRequest.from_dict(tss_key_share_sign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


