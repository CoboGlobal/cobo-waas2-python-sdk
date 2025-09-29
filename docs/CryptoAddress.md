# CryptoAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token identifier (e.g., ETH_USDT, TRON_USDT) that this address is associated with. | 
**crypto_address_id** | **str** | Unique identifier for the pre-approved crypto address, used to reference the address securely in requests. This ID is returned by the system and should be used instead of the raw blockchain address in API calls. | 
**address** | **str** | The actual blockchain address to which funds will be transferred. This is for display purposes only; external clients should always use address_id to refer to the address in secure operations. | 
**label** | **str** | A human-readable label or alias for the crypto address, set by the merchant or platform operator. This field is optional and intended to help distinguish addresses by usage or purpose (e.g., \&quot;Main Payout Wallet\&quot;, \&quot;Cold Wallet\&quot;). | [optional] 
**created_timestamp** | **int** | The created time of the crypto address, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The updated time of the crypto address, represented as a UNIX timestamp in seconds. | [optional] 

## Example

```python
from cobo_waas2.models.crypto_address import CryptoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoAddress from a JSON string
crypto_address_instance = CryptoAddress.from_json(json)
# print the JSON string representation of the object
print(CryptoAddress.to_json())

# convert the object into a dict
crypto_address_dict = crypto_address_instance.to_dict()
# create an instance of CryptoAddress from a dict
crypto_address_from_dict = CryptoAddress.from_dict(crypto_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


