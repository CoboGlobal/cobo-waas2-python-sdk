# SmartContractWalletInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**name** | **str** | The wallet name. | 
**org_id** | **str** | The ID of the owning organization. | 
**chain_id** | **str** | The ID of the chain on which the wallet operates. | [optional] 
**smart_contract_wallet_type** | [**SmartContractWalletType**](SmartContractWalletType.md) |  | 
**safe_address** | **str** | The Smart Contract Wallet address. | [optional] 
**signers** | **List[str]** | The signers of the Smart Contract Wallet. | [optional] 
**threshold** | **int** | The minimum number of confirmations required for the Smart Contract Wallet.  | [optional] 
**cobo_safe_address** | **str** | The address of Cobo Safe. | [optional] 
**initiator** | [**SmartContractInitiator**](SmartContractInitiator.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.smart_contract_wallet_info import SmartContractWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SmartContractWalletInfo from a JSON string
smart_contract_wallet_info_instance = SmartContractWalletInfo.from_json(json)
# print the JSON string representation of the object
print(SmartContractWalletInfo.to_json())

# convert the object into a dict
smart_contract_wallet_info_dict = smart_contract_wallet_info_instance.to_dict()
# create an instance of SmartContractWalletInfo from a dict
smart_contract_wallet_info_from_dict = SmartContractWalletInfo.from_dict(smart_contract_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


