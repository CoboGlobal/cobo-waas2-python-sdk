# TransactionDepositFromLoopSource

Information about the transaction source type `DepositFromLoop`. Refer to [Transaction sources and destinations](/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 

## Example

```python
from cobo_waas2.models.transaction_deposit_from_loop_source import TransactionDepositFromLoopSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDepositFromLoopSource from a JSON string
transaction_deposit_from_loop_source_instance = TransactionDepositFromLoopSource.from_json(json)
# print the JSON string representation of the object
print(TransactionDepositFromLoopSource.to_json())

# convert the object into a dict
transaction_deposit_from_loop_source_dict = transaction_deposit_from_loop_source_instance.to_dict()
# create an instance of TransactionDepositFromLoopSource from a dict
transaction_deposit_from_loop_source_from_dict = TransactionDepositFromLoopSource.from_dict(transaction_deposit_from_loop_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


