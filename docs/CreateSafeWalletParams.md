# CreateSafeWalletParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The wallet name. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**enable_auto_sweep** | **bool** | Enable the auto-sweep feature for the wallet. This parameter only applies to MPC Wallets and Web3 Wallets. | [optional] 
**chain_id** | **str** | The ID of the chain that the wallet operates on. | 
**smart_contract_wallet_type** | [**SmartContractWalletType**](SmartContractWalletType.md) |  | 
**safe_address** | **str** | The address of the Smart Contract Wallet. If this is not provided, Cobo will create a new Safe{Wallet} and set up Cobo Safe for you. In that case, the &#x60;threshold&#x60; and &#x60;signers&#x60; properties are required. | [optional] 
**signers** | **List[str]** | The signers of the Smart Contract Wallet. This property is required when creating a new Safe{Wallet}. | [optional] 
**threshold** | **int** | The minimum number of confirmations required for the Smart Contract Wallet. This property is required when creating a new Safe{Wallet}. | [optional] 
**cobo_safe_address** | **str** | The address of Cobo Safe. If you are importing an existing Safe{Wallet}, Cobo Safe must have been created and enabled. | [optional] 
**initiator** | [**SmartContractInitiator**](SmartContractInitiator.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_safe_wallet_params import CreateSafeWalletParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSafeWalletParams from a JSON string
create_safe_wallet_params_instance = CreateSafeWalletParams.from_json(json)
# print the JSON string representation of the object
print(CreateSafeWalletParams.to_json())

# convert the object into a dict
create_safe_wallet_params_dict = create_safe_wallet_params_instance.to_dict()
# create an instance of CreateSafeWalletParams from a dict
create_safe_wallet_params_from_dict = CreateSafeWalletParams.from_dict(create_safe_wallet_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


