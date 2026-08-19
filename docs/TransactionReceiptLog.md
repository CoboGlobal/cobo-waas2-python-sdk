# TransactionReceiptLog

The information about an event log emitted during the execution of a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_index** | **int** | The index position of the log within the block. | 
**address** | **str** | The address of the contract that emitted the log. | 
**topics** | **List[str]** | The indexed log arguments. The first topic is the hash of the event signature, and the remaining topics are the indexed event parameters, with a maximum of three. | 
**data** | **str** | The non-indexed log arguments, encoded as a hexadecimal string. | 
**block_number** | **int** | The number of the block that contains the log. | [optional] 
**block_hash** | **str** | The hash of the block that contains the log. | [optional] 
**transaction_hash** | **str** | The hash of the transaction that emitted the log. | [optional] 
**transaction_index** | **int** | The index position within the block of the transaction that emitted the log. | [optional] 
**removed** | **bool** | Whether the log was removed due to a chain reorganization. - &#x60;true&#x60;: The log was removed because the block that contains it was reorganized out of the canonical chain. - &#x60;false&#x60;: The log is still valid.  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_receipt_log import TransactionReceiptLog

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReceiptLog from a JSON string
transaction_receipt_log_instance = TransactionReceiptLog.from_json(json)
# print the JSON string representation of the object
print(TransactionReceiptLog.to_json())

# convert the object into a dict
transaction_receipt_log_dict = transaction_receipt_log_instance.to_dict()
# create an instance of TransactionReceiptLog from a dict
transaction_receipt_log_from_dict = TransactionReceiptLog.from_dict(transaction_receipt_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


