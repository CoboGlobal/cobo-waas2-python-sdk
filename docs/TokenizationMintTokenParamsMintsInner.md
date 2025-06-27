# TokenizationMintTokenParamsMintsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount of tokens to mint for this recipient. | 
**to_address** | **str** | The address to mint tokens to for this recipient. | 

## Example

```python
from cobo_waas2.models.tokenization_mint_token_params_mints_inner import TokenizationMintTokenParamsMintsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationMintTokenParamsMintsInner from a JSON string
tokenization_mint_token_params_mints_inner_instance = TokenizationMintTokenParamsMintsInner.from_json(json)
# print the JSON string representation of the object
print(TokenizationMintTokenParamsMintsInner.to_json())

# convert the object into a dict
tokenization_mint_token_params_mints_inner_dict = tokenization_mint_token_params_mints_inner_instance.to_dict()
# create an instance of TokenizationMintTokenParamsMintsInner from a dict
tokenization_mint_token_params_mints_inner_from_dict = TokenizationMintTokenParamsMintsInner.from_dict(tokenization_mint_token_params_mints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


