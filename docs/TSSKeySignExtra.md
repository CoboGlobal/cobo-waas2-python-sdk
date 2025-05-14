# TSSKeySignExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org** | [**OrgInfo**](OrgInfo.md) |  | [optional] 
**project** | [**MPCProject**](MPCProject.md) |  | [optional] 
**vault** | [**MPCVault**](MPCVault.md) |  | [optional] 
**wallet** | [**MPCWalletInfo**](MPCWalletInfo.md) |  | [optional] 
**signer_key_share_holder_group** | [**KeyShareHolderGroup**](KeyShareHolderGroup.md) |  | [optional] 
**source_addresses** | [**List[AddressInfo]**](AddressInfo.md) |  | [optional] 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_sign_extra import TSSKeySignExtra

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeySignExtra from a JSON string
tss_key_sign_extra_instance = TSSKeySignExtra.from_json(json)
# print the JSON string representation of the object
print(TSSKeySignExtra.to_json())

# convert the object into a dict
tss_key_sign_extra_dict = tss_key_sign_extra_instance.to_dict()
# create an instance of TSSKeySignExtra from a dict
tss_key_sign_extra_from_dict = TSSKeySignExtra.from_dict(tss_key_sign_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


