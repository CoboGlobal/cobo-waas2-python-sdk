# TransactionFuelingInfo

Details of the auto-fueling transaction that provides gas for the current transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID of the transaction. | [optional] 
**transaction_id** | **str** | The transaction ID. | [optional] 
**main_transaction_id** | **str** | The UUID of the parent (main) transaction that this record is associated with. Set only when the current record is a gas/fee transaction initiated by FeeStation; omit for main transactions. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_fueling_info import TransactionFuelingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFuelingInfo from a JSON string
transaction_fueling_info_instance = TransactionFuelingInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionFuelingInfo.to_json())

# convert the object into a dict
transaction_fueling_info_dict = transaction_fueling_info_instance.to_dict()
# create an instance of TransactionFuelingInfo from a dict
transaction_fueling_info_from_dict = TransactionFuelingInfo.from_dict(transaction_fueling_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


