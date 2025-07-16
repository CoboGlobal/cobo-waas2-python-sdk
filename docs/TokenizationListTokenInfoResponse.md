# TokenizationListTokenInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenizationTokenInfo]**](TokenizationTokenInfo.md) | List tokens. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_list_token_info_response import TokenizationListTokenInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationListTokenInfoResponse from a JSON string
tokenization_list_token_info_response_instance = TokenizationListTokenInfoResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationListTokenInfoResponse.to_json())

# convert the object into a dict
tokenization_list_token_info_response_dict = tokenization_list_token_info_response_instance.to_dict()
# create an instance of TokenizationListTokenInfoResponse from a dict
tokenization_list_token_info_response_from_dict = TokenizationListTokenInfoResponse.from_dict(tokenization_list_token_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


