# BookkeepingSummary

The bookkeeping item information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_transaction_count** | **int** | Total transaction count. | 
**total_inflow_value** | **str** | The USD value of the inflow. | 
**total_outflow_value** | **str** | The USD value of the outflow. | 
**total_fee_value** | **str** | The USD value of the fee. | [optional] 

## Example

```python
from cobo_waas2.models.bookkeeping_summary import BookkeepingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BookkeepingSummary from a JSON string
bookkeeping_summary_instance = BookkeepingSummary.from_json(json)
# print the JSON string representation of the object
print(BookkeepingSummary.to_json())

# convert the object into a dict
bookkeeping_summary_dict = bookkeeping_summary_instance.to_dict()
# create an instance of BookkeepingSummary from a dict
bookkeeping_summary_from_dict = BookkeepingSummary.from_dict(bookkeeping_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


