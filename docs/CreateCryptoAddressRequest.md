# CreateCryptoAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID that identifies the cryptocurrency and its corresponding blockchain.  **Supported values**:   - **USDC**: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60;   - **USDT**: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**address** | **str** | The actual blockchain address to be used for payouts or transfers. It must be a valid address on the blockchain associated with the specified &#x60;token_id&#x60;.  | 
**label** | **str** | An optional label or alias to help identify the address&#39;s purpose. For example: &#x60;&#39;Main Payout Wallet&#39;&#x60;, &#x60;&#39;Cold Storage&#39;&#x60;. This field is for internal reference only.  | [optional] 

## Example

```python
from cobo_waas2.models.create_crypto_address_request import CreateCryptoAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCryptoAddressRequest from a JSON string
create_crypto_address_request_instance = CreateCryptoAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCryptoAddressRequest.to_json())

# convert the object into a dict
create_crypto_address_request_dict = create_crypto_address_request_instance.to_dict()
# create an instance of CreateCryptoAddressRequest from a dict
create_crypto_address_request_from_dict = CreateCryptoAddressRequest.from_dict(create_crypto_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


