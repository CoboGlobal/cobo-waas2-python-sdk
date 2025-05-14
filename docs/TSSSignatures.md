# TSSSignatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signatures** | [**List[TSSSignature]**](TSSSignature.md) |  | [optional] 
**signature_type** | [**TSSSignatureType**](TSSSignatureType.md) |  | [optional] 
**tss_protocol** | [**TSSProtocol**](TSSProtocol.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_signatures import TSSSignatures

# TODO update the JSON string below
json = "{}"
# create an instance of TSSSignatures from a JSON string
tss_signatures_instance = TSSSignatures.from_json(json)
# print the JSON string representation of the object
print(TSSSignatures.to_json())

# convert the object into a dict
tss_signatures_dict = tss_signatures_instance.to_dict()
# create an instance of TSSSignatures from a dict
tss_signatures_from_dict = TSSSignatures.from_dict(tss_signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


