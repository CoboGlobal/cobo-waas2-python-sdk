# TSSKeySignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The TSS key share group ID. | [optional] 
**root_pub_key** | **str** | The The old TSS key share group&#39;s root extended public key. | [optional] 
**used_node_ids** | **List[str]** |  | [optional] 
**bip32_path_list** | **List[str]** |  | [optional] 
**msg_hash_list** | **List[str]** |  | [optional] 
**tweak_list** | **List[str]** |  | [optional] 
**signature_type** | [**TSSSignatureType**](TSSSignatureType.md) |  | [optional] 
**tss_protocol** | [**TSSProtocol**](TSSProtocol.md) |  | [optional] 
**task_id** | **str** | The task ID. | [optional] 
**biz_task_id** | **str** | The business task ID. This field contains the transaction ID. | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_sign_request import TSSKeySignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeySignRequest from a JSON string
tss_key_sign_request_instance = TSSKeySignRequest.from_json(json)
# print the JSON string representation of the object
print(TSSKeySignRequest.to_json())

# convert the object into a dict
tss_key_sign_request_dict = tss_key_sign_request_instance.to_dict()
# create an instance of TSSKeySignRequest from a dict
tss_key_sign_request_from_dict = TSSKeySignRequest.from_dict(tss_key_sign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


