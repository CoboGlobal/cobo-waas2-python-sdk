# TransactionBlockInfo

The information about the transaction block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_number** | **int** | The block number. | [optional] 
**block_time** | **int** | The time when the block was created, in Unix timestamp format, measured in milliseconds. | [optional] 
**block_hash** | **str** | The block hash. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_block_info import TransactionBlockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBlockInfo from a JSON string
transaction_block_info_instance = TransactionBlockInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionBlockInfo.to_json())

# convert the object into a dict
transaction_block_info_dict = transaction_block_info_instance.to_dict()
# create an instance of TransactionBlockInfo from a dict
transaction_block_info_from_dict = TransactionBlockInfo.from_dict(transaction_block_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


