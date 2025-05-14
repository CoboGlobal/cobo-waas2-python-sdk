# TSSKeyReshareExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org** | [**OrgInfo**](OrgInfo.md) |  | [optional] 
**project** | [**MPCProject**](MPCProject.md) |  | [optional] 
**vault** | [**MPCVault**](MPCVault.md) |  | [optional] 
**source_key_share_holder_group** | [**KeyShareHolderGroup**](KeyShareHolderGroup.md) |  | [optional] 
**target_key_share_holder_group** | [**KeyShareHolderGroup**](KeyShareHolderGroup.md) |  | [optional] 
**tss_request** | [**TSSRequest**](TSSRequest.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_reshare_extra import TSSKeyReshareExtra

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyReshareExtra from a JSON string
tss_key_reshare_extra_instance = TSSKeyReshareExtra.from_json(json)
# print the JSON string representation of the object
print(TSSKeyReshareExtra.to_json())

# convert the object into a dict
tss_key_reshare_extra_dict = tss_key_reshare_extra_instance.to_dict()
# create an instance of TSSKeyReshareExtra from a dict
tss_key_reshare_extra_from_dict = TSSKeyReshareExtra.from_dict(tss_key_reshare_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


