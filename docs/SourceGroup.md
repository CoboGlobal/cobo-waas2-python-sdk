# SourceGroup

The source key share holder group.  **Note:** `source_key_share_holder_group` is used only when `type` is set to either `KeyGenfromKeyGroup` or `Recovery`. This is to specify the key share holder group to be used as the source key share holder group to create key shares for the `target_key_share_holder_group`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_share_holder_group_id** | **str** | The ID of the Source Group. | 
**tss_node_ids** | **List[str]** | The TSS Node IDs participating in creating a new key share holder group when &#x60;type&#x60; is set to either &#x60;KeyGenFromKeyGroup&#x60; or &#x60;Recovery&#x60;.   **Note:** In any [Threshold Signature Schemes (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss) such as the 2-2, 2-3, and 3-3 schemes (in the \&quot;threshold - node count\&quot; format), for &#x60;tss_node_ids&#x60;, you only need to fill in 1 Cobo TSS Node ID and enough non-Cobo TSS Node IDs to satisfy the number of approvers specified in &#x60;threshold&#x60;. To obtain the Cobo TSS Node ID, run [List all Cobo key share holders](/v2/api-references/wallets--mpc-wallets/list-all-cobo-key-share-holders).  | [optional] 

## Example

```python
from cobo_waas2.models.source_group import SourceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SourceGroup from a JSON string
source_group_instance = SourceGroup.from_json(json)
# print the JSON string representation of the object
print(SourceGroup.to_json())

# convert the object into a dict
source_group_dict = source_group_instance.to_dict()
# create an instance of SourceGroup from a dict
source_group_from_dict = SourceGroup.from_dict(source_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


