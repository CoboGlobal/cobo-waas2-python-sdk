# TransactionApprover

The approver data for transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The approver name of the transaction. | [optional] 
**status** | **str** | The approval status. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_approver import TransactionApprover

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionApprover from a JSON string
transaction_approver_instance = TransactionApprover.from_json(json)
# print the JSON string representation of the object
print(TransactionApprover.to_json())

# convert the object into a dict
transaction_approver_dict = transaction_approver_instance.to_dict()
# create an instance of TransactionApprover from a dict
transaction_approver_from_dict = TransactionApprover.from_dict(transaction_approver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


