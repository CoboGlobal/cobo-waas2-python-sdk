# TokenizationPauseTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_pause_token_params import TokenizationPauseTokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationPauseTokenParams from a JSON string
tokenization_pause_token_params_instance = TokenizationPauseTokenParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationPauseTokenParams.to_json())

# convert the object into a dict
tokenization_pause_token_params_dict = tokenization_pause_token_params_instance.to_dict()
# create an instance of TokenizationPauseTokenParams from a dict
tokenization_pause_token_params_from_dict = TokenizationPauseTokenParams.from_dict(tokenization_pause_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


