# UpdateWalletParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**name** | **str** | The wallet name. | [optional] 
**apikey** | **str** | The API key of your exchange account. This property is required when updating the information of an Exchange Wallet. | [optional] 
**secret** | **str** | The API secret of your exchange account. This property is required when updating the information of an Exchange Wallet. | [optional] 
**passphrase** | **str** | The passphrase of your exchange account. | [optional] 
**memo** | **str** | The memo you use when applying for the API key of your exchange account. | [optional] 
**account_identify** | **str** | The identifier of your exchange account. - For Binance, this is email address of your exchange account. - For OKX, this is the user name of your exchange account.  | [optional] 
**ga_code** | **str** | The GA code for the exchange. | [optional] 
**main_wallet_id** | **str** | The ID of the Exchange Wallet (Main Account). | [optional] 

## Example

```python
from cobo_waas2.models.update_wallet_params import UpdateWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWalletParams from a JSON string
update_wallet_params_instance = UpdateWalletParams.from_json(json)
# print the JSON string representation of the object
print(UpdateWalletParams.to_json())

# convert the object into a dict
update_wallet_params_dict = update_wallet_params_instance.to_dict()
# create an instance of UpdateWalletParams from a dict
update_wallet_params_from_dict = UpdateWalletParams.from_dict(update_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


