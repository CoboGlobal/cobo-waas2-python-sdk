# ExchangeWalletInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**name** | **str** | The wallet name. | 
**org_id** | **str** | The ID of the owning organization. | 
**apikey** | **str** | The API key of your exchange account. | 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | 
**parent_wallet_id** | **str** | The wallet ID of the Main Account associated with the Sub Account. This property is returned only if you are creating or querying an Exchange Wallet (Sub Account). | [optional] 
**sub_accounts** | [**List[ExchangeWalletInfoAllOfSubAccounts]**](ExchangeWalletInfoAllOfSubAccounts.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.exchange_wallet_info import ExchangeWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeWalletInfo from a JSON string
exchange_wallet_info_instance = ExchangeWalletInfo.from_json(json)
# print the JSON string representation of the object
print(ExchangeWalletInfo.to_json())

# convert the object into a dict
exchange_wallet_info_dict = exchange_wallet_info_instance.to_dict()
# create an instance of ExchangeWalletInfo from a dict
exchange_wallet_info_from_dict = ExchangeWalletInfo.from_dict(exchange_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


