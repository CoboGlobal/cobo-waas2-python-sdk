# TSSKeyShareSignSignatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signatures** | [**List[TSSKeyShareSignSignature]**](TSSKeyShareSignSignature.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_share_sign_signatures import TSSKeyShareSignSignatures

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyShareSignSignatures from a JSON string
tss_key_share_sign_signatures_instance = TSSKeyShareSignSignatures.from_json(json)
# print the JSON string representation of the object
print(TSSKeyShareSignSignatures.to_json())

# convert the object into a dict
tss_key_share_sign_signatures_dict = tss_key_share_sign_signatures_instance.to_dict()
# create an instance of TSSKeyShareSignSignatures from a dict
tss_key_share_sign_signatures_from_dict = TSSKeyShareSignSignatures.from_dict(tss_key_share_sign_signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


