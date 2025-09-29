# TokenListing

Detailed information about a token listing request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier of the token listing request | 
**chain_id** | **str** | chain_id of the blockchain where the token exists | 
**contract_address** | **str** | Contract address of the token | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**token** | [**TokenInfo**](TokenInfo.md) |  | [optional] 
**status** | [**TokenListingRequestStatus**](TokenListingRequestStatus.md) |  | 
**source** | [**TokenListingRequestSource**](TokenListingRequestSource.md) |  | [optional] 
**feedback** | **str** | Feedback provided by the admin for rejected requests | [optional] 
**created_timestamp** | **int** | Timestamp when the request was created (in milliseconds since Unix epoch) | [optional] 
**updated_timestamp** | **int** | Timestamp when the request was last updated (in milliseconds since Unix epoch) | [optional] 

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


