# TokenizationMintTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**mints** | [**List[TokenizationMintTokenParamsMintsInner]**](TokenizationMintTokenParamsMintsInner.md) | Details for each token mint, including amount and address to mint to. | 
**app_initiator** | **str** | The initiator of the tokenization activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_mint_token_request import TokenizationMintTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationMintTokenRequest from a JSON string
tokenization_mint_token_request_instance = TokenizationMintTokenRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationMintTokenRequest.to_json())

# convert the object into a dict
tokenization_mint_token_request_dict = tokenization_mint_token_request_instance.to_dict()
# create an instance of TokenizationMintTokenRequest from a dict
tokenization_mint_token_request_from_dict = TokenizationMintTokenRequest.from_dict(tokenization_mint_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


