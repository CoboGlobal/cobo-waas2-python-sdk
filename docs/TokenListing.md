# TokenListing

Detailed information about a token listing request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The unique identifier of the token listing request. | 
**chain_id** | **str** | The ID of the blockchain where the token is deployed. | 
**contract_address** | **str** | The token&#39;s contract address on the specified blockchain. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**token** | [**TokenInfo**](TokenInfo.md) |  | [optional] 
**status** | [**TokenListingRequestStatus**](TokenListingRequestStatus.md) |  | 
**source** | [**TokenListingRequestSource**](TokenListingRequestSource.md) |  | [optional] 
**feedback** | **str** | The feedback provided by Cobo when a token listing request is rejected. | [optional] 
**created_timestamp** | **int** | The time when the request was created in Unix timestamp format, measured in milliseconds. | [optional] 
**updated_timestamp** | **int** | The time when the request was last updated in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.token_listing import TokenListing

# TODO update the JSON string below
json = "{}"
# create an instance of TokenListing from a JSON string
token_listing_instance = TokenListing.from_json(json)
# print the JSON string representation of the object
print(TokenListing.to_json())

# convert the object into a dict
token_listing_dict = token_listing_instance.to_dict()
# create an instance of TokenListing from a dict
token_listing_from_dict = TokenListing.from_dict(token_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


