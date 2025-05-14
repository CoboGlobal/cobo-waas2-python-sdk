# TSSKeyShareSignSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The TSS key share group ID. | [optional] 
**signed_msg** | **str** | The hexadecimal encoded signed message. | [optional] 
**msg_hash** | **str** | The message hash. | [optional] 
**signature** | **str** | The signature. | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_share_sign_signature import TSSKeyShareSignSignature

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyShareSignSignature from a JSON string
tss_key_share_sign_signature_instance = TSSKeyShareSignSignature.from_json(json)
# print the JSON string representation of the object
print(TSSKeyShareSignSignature.to_json())

# convert the object into a dict
tss_key_share_sign_signature_dict = tss_key_share_sign_signature_instance.to_dict()
# create an instance of TSSKeyShareSignSignature from a dict
tss_key_share_sign_signature_from_dict = TSSKeyShareSignSignature.from_dict(tss_key_share_sign_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


