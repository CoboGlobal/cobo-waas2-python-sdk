# TokenizationListActivitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenizationActivityInfo]**](TokenizationActivityInfo.md) | The list of tokenization activities. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_list_activities_response import TokenizationListActivitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationListActivitiesResponse from a JSON string
tokenization_list_activities_response_instance = TokenizationListActivitiesResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationListActivitiesResponse.to_json())

# convert the object into a dict
tokenization_list_activities_response_dict = tokenization_list_activities_response_instance.to_dict()
# create an instance of TokenizationListActivitiesResponse from a dict
tokenization_list_activities_response_from_dict = TokenizationListActivitiesResponse.from_dict(tokenization_list_activities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


