# TokenizationIssuedTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID where the token will be issued. | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**token_params** | [**TokenizationIssueTokenParamsTokenParams**](TokenizationIssueTokenParamsTokenParams.md) |  | 
**app_initiator** | **str** | The address of the app initiator.  | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_issued_token_request import TokenizationIssuedTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationIssuedTokenRequest from a JSON string
tokenization_issued_token_request_instance = TokenizationIssuedTokenRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationIssuedTokenRequest.to_json())

# convert the object into a dict
tokenization_issued_token_request_dict = tokenization_issued_token_request_instance.to_dict()
# create an instance of TokenizationIssuedTokenRequest from a dict
tokenization_issued_token_request_from_dict = TokenizationIssuedTokenRequest.from_dict(tokenization_issued_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


