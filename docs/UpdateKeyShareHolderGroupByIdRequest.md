# UpdateKeyShareHolderGroupByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_key_share_holder_group_action** | [**UpdateGroupAction**](UpdateGroupAction.md) |  | 

## Example

```python
from cobo_waas2.models.update_key_share_holder_group_by_id_request import UpdateKeyShareHolderGroupByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKeyShareHolderGroupByIdRequest from a JSON string
update_key_share_holder_group_by_id_request_instance = UpdateKeyShareHolderGroupByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateKeyShareHolderGroupByIdRequest.to_json())

# convert the object into a dict
update_key_share_holder_group_by_id_request_dict = update_key_share_holder_group_by_id_request_instance.to_dict()
# create an instance of UpdateKeyShareHolderGroupByIdRequest from a dict
update_key_share_holder_group_by_id_request_from_dict = UpdateKeyShareHolderGroupByIdRequest.from_dict(update_key_share_holder_group_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


