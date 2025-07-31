# UpdateWalletParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**name** | **str** | The wallet name. | 
**enable_auto_sweep** | **bool** | Enable the auto sweep feature for the wallet | [optional] 

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


