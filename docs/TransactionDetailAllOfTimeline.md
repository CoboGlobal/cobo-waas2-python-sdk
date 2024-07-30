# TransactionDetailAllOfTimeline

The information about transaction timeline, which lists all statuses that the transaction passes through with timestamps indicating when each status is completed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**finished** | **bool** | Whether the transaction status is completed:   - &#x60;true&#x60;: The transaction status is completed.   - &#x60;false&#x60;: The transaction is currently in the status.  | [optional] 
**finished_time** | **int** | The time when the transaction status is completed in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_detail_all_of_timeline import TransactionDetailAllOfTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetailAllOfTimeline from a JSON string
transaction_detail_all_of_timeline_instance = TransactionDetailAllOfTimeline.from_json(json)
# print the JSON string representation of the object
print(TransactionDetailAllOfTimeline.to_json())

# convert the object into a dict
transaction_detail_all_of_timeline_dict = transaction_detail_all_of_timeline_instance.to_dict()
# create an instance of TransactionDetailAllOfTimeline from a dict
transaction_detail_all_of_timeline_from_dict = TransactionDetailAllOfTimeline.from_dict(transaction_detail_all_of_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


