# TSSKeyShareSignExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org** | [**OrgInfo**](OrgInfo.md) |  | [optional] 
**project** | [**MPCProject**](MPCProject.md) |  | [optional] 
**vault** | [**MPCVault**](MPCVault.md) |  | [optional] 
**wallet** | [**MPCWalletInfo**](MPCWalletInfo.md) |  | [optional] 
**validity_key_share_holder_groups** | [**List[KeyShareHolderGroup]**](KeyShareHolderGroup.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_share_sign_extra import TSSKeyShareSignExtra

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyShareSignExtra from a JSON string
tss_key_share_sign_extra_instance = TSSKeyShareSignExtra.from_json(json)
# print the JSON string representation of the object
print(TSSKeyShareSignExtra.to_json())

# convert the object into a dict
tss_key_share_sign_extra_dict = tss_key_share_sign_extra_instance.to_dict()
# create an instance of TSSKeyShareSignExtra from a dict
tss_key_share_sign_extra_from_dict = TSSKeyShareSignExtra.from_dict(tss_key_share_sign_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


