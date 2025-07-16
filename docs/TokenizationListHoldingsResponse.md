# TokenizationListHoldingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenizationHoldingInfo]**](TokenizationHoldingInfo.md) | List of token holdings. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_list_holdings_response import TokenizationListHoldingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationListHoldingsResponse from a JSON string
tokenization_list_holdings_response_instance = TokenizationListHoldingsResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationListHoldingsResponse.to_json())

# convert the object into a dict
tokenization_list_holdings_response_dict = tokenization_list_holdings_response_instance.to_dict()
# create an instance of TokenizationListHoldingsResponse from a dict
tokenization_list_holdings_response_from_dict = TokenizationListHoldingsResponse.from_dict(tokenization_list_holdings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


