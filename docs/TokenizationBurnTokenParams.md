# TokenizationBurnTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**burns** | [**List[TokenizationBurnTokenParamsBurnsInner]**](TokenizationBurnTokenParamsBurnsInner.md) | Details for each token burn, including amount and address to burn from. | 

## Example

```python
from cobo_waas2.models.tokenization_burn_token_params import TokenizationBurnTokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationBurnTokenParams from a JSON string
tokenization_burn_token_params_instance = TokenizationBurnTokenParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationBurnTokenParams.to_json())

# convert the object into a dict
tokenization_burn_token_params_dict = tokenization_burn_token_params_instance.to_dict()
# create an instance of TokenizationBurnTokenParams from a dict
tokenization_burn_token_params_from_dict = TokenizationBurnTokenParams.from_dict(tokenization_burn_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


