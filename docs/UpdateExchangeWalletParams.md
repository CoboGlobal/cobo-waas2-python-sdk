# UpdateExchangeWalletParams

The information of Exchange Wallets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**name** | **str** | The wallet name. | 

## Example

```python
from cobo_waas2.models.update_exchange_wallet_params import UpdateExchangeWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExchangeWalletParams from a JSON string
update_exchange_wallet_params_instance = UpdateExchangeWalletParams.from_json(json)
# print the JSON string representation of the object
print(UpdateExchangeWalletParams.to_json())

# convert the object into a dict
update_exchange_wallet_params_dict = update_exchange_wallet_params_instance.to_dict()
# create an instance of UpdateExchangeWalletParams from a dict
update_exchange_wallet_params_from_dict = UpdateExchangeWalletParams.from_dict(update_exchange_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


