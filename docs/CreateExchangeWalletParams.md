# CreateExchangeWalletParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The wallet name. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**enable_auto_sweep** | **bool** | Enable the auto-sweep feature for the wallet. This parameter only applies to MPC Wallets and Custodial Wallets (Web3 Wallets). | [optional] 
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
from cobo_waas2.models.create_exchange_wallet_params import CreateExchangeWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExchangeWalletParams from a JSON string
create_exchange_wallet_params_instance = CreateExchangeWalletParams.from_json(json)
# print the JSON string representation of the object
print(CreateExchangeWalletParams.to_json())

# convert the object into a dict
create_exchange_wallet_params_dict = create_exchange_wallet_params_instance.to_dict()
# create an instance of CreateExchangeWalletParams from a dict
create_exchange_wallet_params_from_dict = CreateExchangeWalletParams.from_dict(create_exchange_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


