# TokenizationEstimateFeeRequestOperationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID where the token will be issued. | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**token_params** | [**TokenizationIssueTokenParamsTokenParams**](TokenizationIssueTokenParamsTokenParams.md) |  | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**mints** | [**List[TokenizationMintTokenParamsMintsInner]**](TokenizationMintTokenParamsMintsInner.md) | Details for each token mint, including amount and address to mint to. | 
**token_id** | **str** | The ID of the token. | 
**burns** | [**List[TokenizationBurnTokenParamsBurnsInner]**](TokenizationBurnTokenParamsBurnsInner.md) | Details for each token burn, including amount and address to burn from. | 
**action** | [**TokenizationUpdateAddressAction**](TokenizationUpdateAddressAction.md) |  | 
**addresses** | [**List[TokenizationUpdateBlocklistAddressesParamsAddressesInner]**](TokenizationUpdateBlocklistAddressesParamsAddressesInner.md) | A list of addresses to manage. For &#39;add&#39; operations, notes can be provided. For &#39;remove&#39; operations, notes are ignored. | 
**activation** | **bool** | Whether to activate the allowlist feature for the token. | 
**data** | [**TokenizationContractCallParamsData**](TokenizationContractCallParamsData.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_estimate_fee_request_operation_params import TokenizationEstimateFeeRequestOperationParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationEstimateFeeRequestOperationParams from a JSON string
tokenization_estimate_fee_request_operation_params_instance = TokenizationEstimateFeeRequestOperationParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationEstimateFeeRequestOperationParams.to_json())

# convert the object into a dict
tokenization_estimate_fee_request_operation_params_dict = tokenization_estimate_fee_request_operation_params_instance.to_dict()
# create an instance of TokenizationEstimateFeeRequestOperationParams from a dict
tokenization_estimate_fee_request_operation_params_from_dict = TokenizationEstimateFeeRequestOperationParams.from_dict(tokenization_estimate_fee_request_operation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


