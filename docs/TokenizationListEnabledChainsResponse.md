# TokenizationListEnabledChainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** | The list of tokenization supported chains. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_list_enabled_chains_response import TokenizationListEnabledChainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationListEnabledChainsResponse from a JSON string
tokenization_list_enabled_chains_response_instance = TokenizationListEnabledChainsResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationListEnabledChainsResponse.to_json())

# convert the object into a dict
tokenization_list_enabled_chains_response_dict = tokenization_list_enabled_chains_response_instance.to_dict()
# create an instance of TokenizationListEnabledChainsResponse from a dict
tokenization_list_enabled_chains_response_from_dict = TokenizationListEnabledChainsResponse.from_dict(tokenization_list_enabled_chains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


