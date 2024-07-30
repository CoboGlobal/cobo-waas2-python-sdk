# PoolDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique protocol id. | 
**chain_id** | **str** | The unique chain id. | 
**protocol** | **str** | The name of the protocol. | 
**protocol_icon_url** | **str** | The URL of the protocol&#39;s icon. | 
**supported_wallet_types** | [**List[WalletType]**](WalletType.md) | The list of available wallet types. | 
**supported_wallet_subtypes** | [**List[WalletSubtype]**](WalletSubtype.md) | The list of available wallet types. | 
**token_id** | **str** | The unique token id. | 
**est_apr** | **float** | The estimated APR. | 
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | [optional] 
**min_amount** | **str** | The minimum amount to stake. | [optional] 
**max_amount** | **str** | The maximum amount to stake. | [optional] 
**min_stake_period** | **int** | The minimum staking period in days. | [optional] 
**max_stake_period** | **int** | The maximum staking period in days. | [optional] 
**min_stake_blocks** | **int** | The minimum staking blocks. | [optional] 
**max_stake_blocks** | **int** | The maximum staking blocks. | [optional] 
**validators_info** | [**List[PoolDetailsAllOfValidatorsInfo]**](PoolDetailsAllOfValidatorsInfo.md) | The list of validators. | 

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


