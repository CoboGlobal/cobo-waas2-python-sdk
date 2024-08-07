# TransactionTimeline

The information about transaction timeline, which lists all statuses that the transaction passes through with timestamps indicating when each status is completed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**finished** | **bool** | Whether the transaction status is completed:   - &#x60;true&#x60;: The transaction status is completed.   - &#x60;false&#x60;: The transaction is currently in the status.  | [optional] 
**finished_timestamp** | **int** | The time when the transaction status is completed in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_timeline import TransactionTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTimeline from a JSON string
transaction_timeline_instance = TransactionTimeline.from_json(json)
# print the JSON string representation of the object
print(TransactionTimeline.to_json())

# convert the object into a dict
transaction_timeline_dict = transaction_timeline_instance.to_dict()
# create an instance of TransactionTimeline from a dict
transaction_timeline_from_dict = TransactionTimeline.from_dict(transaction_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


