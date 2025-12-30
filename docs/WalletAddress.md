# WalletAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_address_id** | **str** | The wallet address ID. | 
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID of the address. | 
**risk_level** | [**AddressRiskLevel**](AddressRiskLevel.md) |  | [optional] 
**screening_timestamp** | **int** | UNIX timestamp (in seconds) when the address was last screened for compliance. | [optional] 
**updated_timestamp** | **int** | The updated time of the wallet address, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.wallet_address import WalletAddress

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAddress from a JSON string
wallet_address_instance = WalletAddress.from_json(json)
# print the JSON string representation of the object
print(WalletAddress.to_json())

# convert the object into a dict
wallet_address_dict = wallet_address_instance.to_dict()
# create an instance of WalletAddress from a dict
wallet_address_from_dict = WalletAddress.from_dict(wallet_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


