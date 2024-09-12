# PoolDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the staking pool. A staking pool is a pairing of a staking protocol and a specific type of token. | 
**chain_id** | **str** | The chain ID. | 
**protocol** | **str** | The name of the protocol. | 
**protocol_icon_url** | **str** | The URL of the protocol&#39;s icon. | 
**supported_wallet_types** | [**List[WalletType]**](WalletType.md) | The wallet type. Possible values include:  - &#x60;Custodial&#x60;: [Custodial Wallets](https://manuals.cobo.com/en/portal/custodial-wallets/introduction)  - &#x60;MPC&#x60;: [MPC Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction)  - &#x60;SmartContract&#x60;: [Smart Contract Wallets](https://manuals.cobo.com/en/portal/smart-contract-wallets/introduction)  - &#x60;Exchange&#x60;: [Exchange Wallets](https://manuals.cobo.com/en/portal/exchange-wallets/introduction)  | 
**supported_wallet_subtypes** | [**List[WalletSubtype]**](WalletSubtype.md) | The wallet subtype. Possible values include: - &#x60;Asset&#x60;: Custodial Wallets (Asset Wallets). - &#x60;Web3&#x60;: Custodial Wallets (Web3  Wallets). - &#x60;Org-Controlled&#x60;: MPC Wallets (Organization-Controlled Wallets). - &#x60;User-Controlled&#x60;: MPC Wallets (User-Controlled Wallets). - &#x60;Safe{Wallet}&#x60;: Smart Contract Wallets (Safe{Wallet}). - &#x60;Main&#x60;: Exchange Wallets (Main Account). - &#x60;Sub&#x60;: Exchange Wallets (Sub Account).  | 
**token_id** | **str** | The token ID. | 
**est_apr** | **float** | The estimated annual percentage rate (APR). | 
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | [optional] 
**min_amount** | **str** | The minimum amount that can be staked in one staking request. | [optional] 
**max_amount** | **str** | The maximum amount that can be staked in one staking request. | [optional] 
**min_stake_period** | **int** | The minimum staking period, in days. | [optional] 
**max_stake_period** | **int** | The maximum staking period, in days. | [optional] 
**min_stake_blocks** | **int** | The minimum block number. A block number indicates the number of blocks that need to be processed before the locked tokens are unlocked and become accessible. | [optional] 
**max_stake_blocks** | **int** | The maximum block number. A block number indicates the number of blocks that need to be processed before the locked tokens are unlocked and become accessible. | [optional] 
**validators_info** | [**List[PoolDetailsAllOfValidatorsInfo]**](PoolDetailsAllOfValidatorsInfo.md) | A list of available validators. | 

## Example

```python
from cobo_waas2.models.pool_details import PoolDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PoolDetails from a JSON string
pool_details_instance = PoolDetails.from_json(json)
# print the JSON string representation of the object
print(PoolDetails.to_json())

# convert the object into a dict
pool_details_dict = pool_details_instance.to_dict()
# create an instance of PoolDetails from a dict
pool_details_from_dict = PoolDetails.from_dict(pool_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


