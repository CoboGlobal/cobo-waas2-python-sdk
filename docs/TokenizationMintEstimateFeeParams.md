# TokenizationMintEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**mints** | [**List[TokenizationMintTokenParamsMintsInner]**](TokenizationMintTokenParamsMintsInner.md) | Details for each token mint, including amount and address to mint to. | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**token_id** | **str** | The ID of the token. | 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_mint_estimate_fee_params import TokenizationMintEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationMintEstimateFeeParams from a JSON string
tokenization_mint_estimate_fee_params_instance = TokenizationMintEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationMintEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_mint_estimate_fee_params_dict = tokenization_mint_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationMintEstimateFeeParams from a dict
tokenization_mint_estimate_fee_params_from_dict = TokenizationMintEstimateFeeParams.from_dict(tokenization_mint_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


