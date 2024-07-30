# TransactionSignatureResult

The result of a message sign transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | [**TransactionResultType**](TransactionResultType.md) |  | [optional] 
**signature** | **str** | The raw data of the signature. | 

## Example

```python
from cobo_waas2.models.transaction_signature_result import TransactionSignatureResult

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSignatureResult from a JSON string
transaction_signature_result_instance = TransactionSignatureResult.from_json(json)
# print the JSON string representation of the object
print(TransactionSignatureResult.to_json())

# convert the object into a dict
transaction_signature_result_dict = transaction_signature_result_instance.to_dict()
# create an instance of TransactionSignatureResult from a dict
transaction_signature_result_from_dict = TransactionSignatureResult.from_dict(transaction_signature_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


