# TransactionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | [**TransactionResultType**](TransactionResultType.md) |  | [optional] 
**signature** | **str** | The raw data of the signature. | 

## Example

```python
from cobo_waas2.models.transaction_result import TransactionResult

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResult from a JSON string
transaction_result_instance = TransactionResult.from_json(json)
# print the JSON string representation of the object
print(TransactionResult.to_json())

# convert the object into a dict
transaction_result_dict = transaction_result_instance.to_dict()
# create an instance of TransactionResult from a dict
transaction_result_from_dict = TransactionResult.from_dict(transaction_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


