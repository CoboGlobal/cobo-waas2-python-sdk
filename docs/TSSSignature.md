# TSSSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bip32_path** | **str** | The BIP32 path. | [optional] 
**msg_hash** | **str** | The message hash. | [optional] 
**tweak** | **str** | The tweak. | [optional] 
**signature** | **str** | The signature. | [optional] 
**signature_recovery** | **str** | The signature recovery. | [optional] 

## Example

```python
from cobo_waas2.models.tss_signature import TSSSignature

# TODO update the JSON string below
json = "{}"
# create an instance of TSSSignature from a JSON string
tss_signature_instance = TSSSignature.from_json(json)
# print the JSON string representation of the object
print(TSSSignature.to_json())

# convert the object into a dict
tss_signature_dict = tss_signature_instance.to_dict()
# create an instance of TSSSignature from a dict
tss_signature_from_dict = TSSSignature.from_dict(tss_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


