# TransactionReplacement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replaced_by_type** | [**ReplaceType**](ReplaceType.md) |  | [optional] 
**replaced_by_transaction_id** | **str** | The ID of the transaction that this transaction was replaced by. | [optional] 
**replaced_by_transaction_hash** | **str** | The hash of the transaction that this transaction was replaced by. | [optional] 
**replaced_type** | [**ReplaceType**](ReplaceType.md) |  | [optional] 
**replaced_transaction_id** | **str** | The ID of the transaction that this transaction replaced. | [optional] 
**replaced_transaction_hash** | **str** | The hash of the transaction that this transaction replaced. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_replacement import TransactionReplacement

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReplacement from a JSON string
transaction_replacement_instance = TransactionReplacement.from_json(json)
# print the JSON string representation of the object
print(TransactionReplacement.to_json())

# convert the object into a dict
transaction_replacement_dict = transaction_replacement_instance.to_dict()
# create an instance of TransactionReplacement from a dict
transaction_replacement_from_dict = TransactionReplacement.from_dict(transaction_replacement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


