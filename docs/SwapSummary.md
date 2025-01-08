# SwapSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_usd_value** | **str** | The total USD value of the swap activities, represented as a string. | 
**activity_count** | **int** | The total number of swap activities. | 

## Example

```python
from cobo_waas2.models.swap_summary import SwapSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SwapSummary from a JSON string
swap_summary_instance = SwapSummary.from_json(json)
# print the JSON string representation of the object
print(SwapSummary.to_json())

# convert the object into a dict
swap_summary_dict = swap_summary_instance.to_dict()
# create an instance of SwapSummary from a dict
swap_summary_from_dict = SwapSummary.from_dict(swap_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


