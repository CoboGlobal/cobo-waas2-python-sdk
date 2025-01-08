# CreateWalletParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The wallet name. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**vault_id** | **str** | The ID of the owning vault. You can call [List all vaults](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/list-all-vaults) to retrieve all vault IDs under your organization. | 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | 
**apikey** | **str** | The API key of your exchange account. | 
**secret** | **str** | The API secret of your exchange account. | 
**passphrase** | **str** | The passphrase of your exchange account. | [optional] 
**memo** | **str** | The memo you use when applying for the API key of your exchange account. | [optional] 
**account_identify** | **str** | The identifier of your exchange account. - For Binance, this is email address of your exchange account. - For OKX, this is the user name of your exchange account.  | [optional] 
**ga_code** | **str** | The GA code for the exchange. | [optional] 
**main_wallet_id** | **str** | The ID of the Exchange Wallet (Main Account). | [optional] 

## Example

```python
from cobo_waas2.models.create_wallet_params import CreateWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWalletParams from a JSON string
create_wallet_params_instance = CreateWalletParams.from_json(json)
# print the JSON string representation of the object
print(CreateWalletParams.to_json())

# convert the object into a dict
create_wallet_params_dict = create_wallet_params_instance.to_dict()
# create an instance of CreateWalletParams from a dict
create_wallet_params_from_dict = CreateWalletParams.from_dict(create_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


