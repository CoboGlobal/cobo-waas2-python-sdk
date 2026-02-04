# CreateWalletAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID of the cryptocurrency.  Supported values in the development environment:   - Counterparty: &#x60;ARBITRUM_ETH&#x60;, &#x60;BASE_ETH&#x60;, &#x60;BSC_BNB&#x60;, &#x60;ETH&#x60;, &#x60;TRON&#x60;, &#x60;MATIC&#x60;, &#x60;SOL&#x60;, &#x60;TTRON&#x60;, &#x60;SOLDEV_SOL&#x60;, &#x60;SETH&#x60;   - Destination: &#x60;All EVM Networks&#x60;, &#x60;SOL&#x60;, &#x60;TRON&#x60;, &#x60;TTRON&#x60;, &#x60;SOLDEV_SOL&#x60; Supported values in the production environment:   - Counterparty: &#x60;ARBITRUM_ETH&#x60;, &#x60;BASE_ETH&#x60;, &#x60;BSC_BNB&#x60;, &#x60;ETH&#x60;, &#x60;TRON&#x60;, &#x60;MATIC&#x60;, &#x60;SOL&#x60;   - Destination: &#x60;All EVM Networks&#x60;, &#x60;SOL&#x60;, &#x60;TRON&#x60;  | 

## Example

```python
from cobo_waas2.models.create_wallet_address import CreateWalletAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletAddress from a JSON string
create_wallet_address_instance = CreateWalletAddress.from_json(json)
# print the JSON string representation of the object
print(CreateWalletAddress.to_json())

# convert the object into a dict
create_wallet_address_dict = create_wallet_address_instance.to_dict()
# create an instance of CreateWalletAddress from a dict
create_wallet_address_from_dict = CreateWalletAddress.from_dict(create_wallet_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


