# WalletInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**name** | **str** | The wallet name. | 
**org_id** | **str** | The ID of the owning organization. | 
**project_id** | **str** | The project ID. | [optional] 
**vault_id** | **str** | The ID of the owning vault. | 
**apikey** | **str** | The API key of your exchange account. | 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | 
**main_wallet_id** | **str** | The wallet ID of the Main Account associated with the Sub Account. This property is returned only if you are creating or querying an Exchange Wallet (Sub Account). | [optional] 

## Example

```python
from cobo_waas2.models.wallet_info import WalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WalletInfo from a JSON string
wallet_info_instance = WalletInfo.from_json(json)
# print the JSON string representation of the object
print(WalletInfo.to_json())

# convert the object into a dict
wallet_info_dict = wallet_info_instance.to_dict()
# create an instance of WalletInfo from a dict
wallet_info_from_dict = WalletInfo.from_dict(wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


