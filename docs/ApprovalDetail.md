# ApprovalDetail

The approval detail data for transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | [optional] 
**cobo_id** | **str** | The Cobo ID, which can be used to track a transaction. | [optional] 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 
**broker_user** | [**RoleDetail**](RoleDetail.md) |  | [optional] 
**spender** | [**RoleDetail**](RoleDetail.md) |  | [optional] 
**approver** | [**RoleDetail**](RoleDetail.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.approval_detail import ApprovalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalDetail from a JSON string
approval_detail_instance = ApprovalDetail.from_json(json)
# print the JSON string representation of the object
print(ApprovalDetail.to_json())

# convert the object into a dict
approval_detail_dict = approval_detail_instance.to_dict()
# create an instance of ApprovalDetail from a dict
approval_detail_from_dict = ApprovalDetail.from_dict(approval_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


