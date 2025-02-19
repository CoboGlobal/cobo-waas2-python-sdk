# TransactionUserApprovalDetail

The user approval data for transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | The Cobo Guard public key of the user who audited this message. | [optional] 
**result** | [**TransactionApprovalResult**](TransactionApprovalResult.md) |  | [optional] 
**signature** | **str** | The signature of the audited message. | [optional] 
**language** | **str** | The language of the audited message. | [optional] 
**message_version** | **str** | The version of the audited message. | [optional] 
**message** | **str** | The audited message. | [optional] 
**extra_message** | **str** | The extra audited message. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_user_approval_detail import TransactionUserApprovalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUserApprovalDetail from a JSON string
transaction_user_approval_detail_instance = TransactionUserApprovalDetail.from_json(json)
# print the JSON string representation of the object
print(TransactionUserApprovalDetail.to_json())

# convert the object into a dict
transaction_user_approval_detail_dict = transaction_user_approval_detail_instance.to_dict()
# create an instance of TransactionUserApprovalDetail from a dict
transaction_user_approval_detail_from_dict = TransactionUserApprovalDetail.from_dict(transaction_user_approval_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


