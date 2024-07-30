# TransactionRbf

The information about the request to drop or to speed up transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 
**source** | [**TransactionRbfSource**](TransactionRbfSource.md) |  | [optional] 
**category_names** | **List[str]** | The custom category for you to identify your transactions. | [optional] 
**description** | **str** | The description of the RBF transaction. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_rbf import TransactionRbf

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRbf from a JSON string
transaction_rbf_instance = TransactionRbf.from_json(json)
# print the JSON string representation of the object
print(TransactionRbf.to_json())

# convert the object into a dict
transaction_rbf_dict = transaction_rbf_instance.to_dict()
# create an instance of TransactionRbf from a dict
transaction_rbf_from_dict = TransactionRbf.from_dict(transaction_rbf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


