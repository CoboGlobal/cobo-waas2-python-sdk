# ApiLogSummary

The information about an API log.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **str** | A unique identifier for the API log, used for tracking. | [optional] 
**api_method** | **str** | The HTTP method used for the API request. | 
**api_endpoint** | **str** | The endpoint of the API request. | 
**request_timestamp** | **int** | The time when the API request was created, in Unix timestamp format, measured in milliseconds. | 
**status_code** | **int** | The HTTP status code returned by the API request. | 

## Example

```python
from cobo_waas2.models.api_log_summary import ApiLogSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogSummary from a JSON string
api_log_summary_instance = ApiLogSummary.from_json(json)
# print the JSON string representation of the object
print(ApiLogSummary.to_json())

# convert the object into a dict
api_log_summary_dict = api_log_summary_instance.to_dict()
# create an instance of ApiLogSummary from a dict
api_log_summary_from_dict = ApiLogSummary.from_dict(api_log_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


