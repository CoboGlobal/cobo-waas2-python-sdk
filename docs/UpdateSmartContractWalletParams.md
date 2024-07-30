# UpdateSmartContractWalletParams

The information of Smart Contract Wallets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**name** | **str** | The wallet name. | [optional] 

## Example

```python
from cobo_waas2.models.update_smart_contract_wallet_params import UpdateSmartContractWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSmartContractWalletParams from a JSON string
update_smart_contract_wallet_params_instance = UpdateSmartContractWalletParams.from_json(json)
# print the JSON string representation of the object
print(UpdateSmartContractWalletParams.to_json())

# convert the object into a dict
update_smart_contract_wallet_params_dict = update_smart_contract_wallet_params_instance.to_dict()
# create an instance of UpdateSmartContractWalletParams from a dict
update_smart_contract_wallet_params_from_dict = UpdateSmartContractWalletParams.from_dict(update_smart_contract_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


