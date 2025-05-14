# TSSKeyShareSignDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The TSS key share group ID. | [optional] 
**message** | **str** | The message to sign by key share. | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_share_sign_detail import TSSKeyShareSignDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyShareSignDetail from a JSON string
tss_key_share_sign_detail_instance = TSSKeyShareSignDetail.from_json(json)
# print the JSON string representation of the object
print(TSSKeyShareSignDetail.to_json())

# convert the object into a dict
tss_key_share_sign_detail_dict = tss_key_share_sign_detail_instance.to_dict()
# create an instance of TSSKeyShareSignDetail from a dict
tss_key_share_sign_detail_from_dict = TSSKeyShareSignDetail.from_dict(tss_key_share_sign_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


