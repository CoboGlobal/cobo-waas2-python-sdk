# RoleDetail

Transaction approval details response schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ApprovalTransactionResult**](ApprovalTransactionResult.md) |  | [optional] 
**threshold** | **int** | The threshold for the transaction approval. | [optional] 
**user_details** | [**List[ApprovalUserDetail]**](ApprovalUserDetail.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.role_detail import RoleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RoleDetail from a JSON string
role_detail_instance = RoleDetail.from_json(json)
# print the JSON string representation of the object
print(RoleDetail.to_json())

# convert the object into a dict
role_detail_dict = role_detail_instance.to_dict()
# create an instance of RoleDetail from a dict
role_detail_from_dict = RoleDetail.from_dict(role_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


