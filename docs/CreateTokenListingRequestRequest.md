# CreateTokenListingRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**chain_id** | **str** | The ID of the blockchain where the token is deployed. | 
**contract_address** | **str** | The token&#39;s contract address on the specified blockchain. | 

## Example

```python
from cobo_waas2.models.create_token_listing_request_request import CreateTokenListingRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenListingRequestRequest from a JSON string
create_token_listing_request_request_instance = CreateTokenListingRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTokenListingRequestRequest.to_json())

# convert the object into a dict
create_token_listing_request_request_dict = create_token_listing_request_request_instance.to_dict()
# create an instance of CreateTokenListingRequestRequest from a dict
create_token_listing_request_request_from_dict = CreateTokenListingRequestRequest.from_dict(create_token_listing_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


