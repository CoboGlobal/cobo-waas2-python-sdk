# TSSGroups

The data for the TSS key share group ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tss_key_share_group_id** | **str** | The TSS key share group ID. | [optional] 
**curve** | [**CurveType**](CurveType.md) |  | [optional] 
**root_pubkey** | **str** | The vault&#39;s [root extended public key](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/tss-node-deployment#tss-node-on-cobo-portal-and-mpc-root-extended-public-key). | [optional] 

## Example

```python
from cobo_waas2.models.tss_groups import TSSGroups

# TODO update the JSON string below
json = "{}"
# create an instance of TSSGroups from a JSON string
tss_groups_instance = TSSGroups.from_json(json)
# print the JSON string representation of the object
print(TSSGroups.to_json())

# convert the object into a dict
tss_groups_dict = tss_groups_instance.to_dict()
# create an instance of TSSGroups from a dict
tss_groups_from_dict = TSSGroups.from_dict(tss_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


