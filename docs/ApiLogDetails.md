# ApiLogDetails

The information about an API log.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **str** | A unique identifier for the API log, used for tracking. | 
**api_method** | **str** | The HTTP method used for the API request. | 
**api_endpoint** | **str** | The endpoint of the API request. | 
**status_code** | **int** | The HTTP status code returned by the API request. | 
**ip_address** | **str** | The client&#39;s IP address that made the API request. | 
**request_timestamp** | **int** | The time when the API request was created, in Unix timestamp format, measured in milliseconds. | 
**api_key** | **str** | The API key used to call the API. For more details, refer to [API key](https://www.cobo.com/developers/v2/guides/overview/cobo-auth#api-key). | 
**response_body** | **str** | The response body of the API request. | 
**var_query_params** | **str** | The query parameters of the API request. | 
**request_body** | **str** | The request body of the API request. | 

## Example

```python
from cobo_waas2.models.api_log_details import ApiLogDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogDetails from a JSON string
api_log_details_instance = ApiLogDetails.from_json(json)
# print the JSON string representation of the object
print(ApiLogDetails.to_json())

# convert the object into a dict
api_log_details_dict = api_log_details_instance.to_dict()
# create an instance of ApiLogDetails from a dict
api_log_details_from_dict = ApiLogDetails.from_dict(api_log_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


