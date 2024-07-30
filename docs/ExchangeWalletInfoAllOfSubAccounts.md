# ExchangeWalletInfoAllOfSubAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID of the Sub Account. This property is returned only if you are creating or querying an Exchange Wallet (Main Account). | 
**account_id** | **str** | The Sub Account ID. It can be an email address, a user name, or a custom account ID. This property is returned only if you are creating or querying an Exchange Wallet (Main Account). | 

## Example

```python
from cobo_waas2.models.exchange_wallet_info_all_of_sub_accounts import ExchangeWalletInfoAllOfSubAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeWalletInfoAllOfSubAccounts from a JSON string
exchange_wallet_info_all_of_sub_accounts_instance = ExchangeWalletInfoAllOfSubAccounts.from_json(json)
# print the JSON string representation of the object
print(ExchangeWalletInfoAllOfSubAccounts.to_json())

# convert the object into a dict
exchange_wallet_info_all_of_sub_accounts_dict = exchange_wallet_info_all_of_sub_accounts_instance.to_dict()
# create an instance of ExchangeWalletInfoAllOfSubAccounts from a dict
exchange_wallet_info_all_of_sub_accounts_from_dict = ExchangeWalletInfoAllOfSubAccounts.from_dict(exchange_wallet_info_all_of_sub_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


