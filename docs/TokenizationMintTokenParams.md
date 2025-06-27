# TokenizationMintTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**mints** | [**List[TokenizationMintTokenParamsMintsInner]**](TokenizationMintTokenParamsMintsInner.md) | Details for each token mint, including amount and address to mint to. | 

## Example

```python
from cobo_waas2.models.tokenization_mint_token_params import TokenizationMintTokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationMintTokenParams from a JSON string
tokenization_mint_token_params_instance = TokenizationMintTokenParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationMintTokenParams.to_json())

# convert the object into a dict
tokenization_mint_token_params_dict = tokenization_mint_token_params_instance.to_dict()
# create an instance of TokenizationMintTokenParams from a dict
tokenization_mint_token_params_from_dict = TokenizationMintTokenParams.from_dict(tokenization_mint_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


