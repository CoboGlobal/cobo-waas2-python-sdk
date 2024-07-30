# TransactionSigner

The signer data for transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer** | **str** | The signer name of the transaction. | [optional] 
**status** | **str** | The signing status. | [optional] 
**failed_reason** | **str** | Failed reason of signing process. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_signer import TransactionSigner

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSigner from a JSON string
transaction_signer_instance = TransactionSigner.from_json(json)
# print the JSON string representation of the object
print(TransactionSigner.to_json())

# convert the object into a dict
transaction_signer_dict = transaction_signer_instance.to_dict()
# create an instance of TransactionSigner from a dict
transaction_signer_from_dict = TransactionSigner.from_dict(transaction_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


