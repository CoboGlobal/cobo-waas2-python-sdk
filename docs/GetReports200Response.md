# GetReports200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Report]**](Report.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.get_reports200_response import GetReports200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReports200Response from a JSON string
get_reports200_response_instance = GetReports200Response.from_json(json)
# print the JSON string representation of the object
print(GetReports200Response.to_json())

# convert the object into a dict
get_reports200_response_dict = get_reports200_response_instance.to_dict()
# create an instance of GetReports200Response from a dict
get_reports200_response_from_dict = GetReports200Response.from_dict(get_reports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


