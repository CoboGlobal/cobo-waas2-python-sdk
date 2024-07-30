# MpcSigningGroup

The information about the Signing Group of an MPC Wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_key_share_holder_group_id** | **str** | The ID of the Signing Group. | [optional] 
**used_tss_node_ids** | **List[str]** | The ID of the TSS Nodes that are required to participate in the signature. | [optional] 

## Example

```python
from cobo_waas2.models.mpc_signing_group import MpcSigningGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MpcSigningGroup from a JSON string
mpc_signing_group_instance = MpcSigningGroup.from_json(json)
# print the JSON string representation of the object
print(MpcSigningGroup.to_json())

# convert the object into a dict
mpc_signing_group_dict = mpc_signing_group_instance.to_dict()
# create an instance of MpcSigningGroup from a dict
mpc_signing_group_from_dict = MpcSigningGroup.from_dict(mpc_signing_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


