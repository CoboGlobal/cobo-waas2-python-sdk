# CreatedWalletInfo


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
from cobo_waas2.models.created_wallet_info import CreatedWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedWalletInfo from a JSON string
created_wallet_info_instance = CreatedWalletInfo.from_json(json)
# print the JSON string representation of the object
print(CreatedWalletInfo.to_json())

# convert the object into a dict
created_wallet_info_dict = created_wallet_info_instance.to_dict()
# create an instance of CreatedWalletInfo from a dict
created_wallet_info_from_dict = CreatedWalletInfo.from_dict(created_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


