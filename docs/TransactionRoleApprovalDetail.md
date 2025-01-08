# TransactionRoleApprovalDetail

The role approval data for transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TransactionApprovalResult**](TransactionApprovalResult.md) |  | [optional] 
**review_threshold** | **int** | The threshold for passing the review of this role. | [optional] 
**initiator** | **str** | The initiator of the transaction. | [optional] 
**complete_time** | **str** | Time to complete the review. | [optional] 
**user_details** | [**List[TransactionUserApprovalDetail]**](TransactionUserApprovalDetail.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_role_approval_detail import TransactionRoleApprovalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRoleApprovalDetail from a JSON string
transaction_role_approval_detail_instance = TransactionRoleApprovalDetail.from_json(json)
# print the JSON string representation of the object
print(TransactionRoleApprovalDetail.to_json())

# convert the object into a dict
transaction_role_approval_detail_dict = transaction_role_approval_detail_instance.to_dict()
# create an instance of TransactionRoleApprovalDetail from a dict
transaction_role_approval_detail_from_dict = TransactionRoleApprovalDetail.from_dict(transaction_role_approval_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


