# ApprovalDetail

Details of the transaction approval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID. | [optional] 
**cobo_id** | **str** | Cobo ID used to track a transaction. | [optional] 
**request_id** | **str** | Request ID used to track a transaction request. | [optional] 
**address_owner** | [**RoleDetail**](RoleDetail.md) |  | [optional] 
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


