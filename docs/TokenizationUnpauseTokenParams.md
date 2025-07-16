# TokenizationUnpauseTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_unpause_token_params import TokenizationUnpauseTokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUnpauseTokenParams from a JSON string
tokenization_unpause_token_params_instance = TokenizationUnpauseTokenParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationUnpauseTokenParams.to_json())

# convert the object into a dict
tokenization_unpause_token_params_dict = tokenization_unpause_token_params_instance.to_dict()
# create an instance of TokenizationUnpauseTokenParams from a dict
tokenization_unpause_token_params_from_dict = TokenizationUnpauseTokenParams.from_dict(tokenization_unpause_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


