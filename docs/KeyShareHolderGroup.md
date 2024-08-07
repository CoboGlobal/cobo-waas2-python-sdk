# KeyShareHolderGroup

The data for key share holder group information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_share_holder_group_id** | **str** | The key share holder group ID. | [optional] 
**type** | [**KeyShareHolderGroupType**](KeyShareHolderGroupType.md) |  | [optional] 
**tss_key_share_groups** | [**List[TSSGroups]**](TSSGroups.md) |  | [optional] 
**key_share_holders** | [**List[KeyShareHolder]**](KeyShareHolder.md) |  | [optional] 
**participants** | **int** | The number of key share holders in this key share holder group. | [optional] 
**threshold** | **int** | The number of key share holders required to approve each operation in this key share holder group. | [optional] 
**status** | [**KeyShareHolderGroupStatus**](KeyShareHolderGroupStatus.md) |  | [optional] 
**created_timestamp** | **int** | The key share holder group&#39;s creation time in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.key_share_holder_group import KeyShareHolderGroup

# TODO update the JSON string below
json = "{}"
# create an instance of KeyShareHolderGroup from a JSON string
key_share_holder_group_instance = KeyShareHolderGroup.from_json(json)
# print the JSON string representation of the object
print(KeyShareHolderGroup.to_json())

# convert the object into a dict
key_share_holder_group_dict = key_share_holder_group_instance.to_dict()
# create an instance of KeyShareHolderGroup from a dict
key_share_holder_group_from_dict = KeyShareHolderGroup.from_dict(key_share_holder_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


