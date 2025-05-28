# CreateStakeActivityExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**finality_provider_public_key** | **str** | The public key of the finality provider. | 
**stake_block_time** | **int** | The number of blocks that need to be processed before the locked tokens are unlocked and become accessible. | 
**auto_broadcast** | **bool** | Whether to automatically broadcast the transaction. The default value is &#x60;true&#x60;.  - &#x60;true&#x60;: Automatically broadcast the transaction. - &#x60;false&#x60;: The transaction will not be submitted to the blockchain automatically. You can call [Broadcast signed transactions](https://www.cobo.com/developers/v2/api-references/transactions/broadcast-signed-transactions) to broadcast the transaction to the blockchain, or retrieve the signed raw transaction data &#x60;raw_tx&#x60; by calling [Get transaction information](https://www.cobo.com/developers/v2/api-references/transactions/get-transaction-information) and broadcast it yourself.  | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**provider_name** | **str** | The name of the provider. | 
**timelock** | **int** | The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal. | 
**change_address** | **str** | The change address on the Bitcoin chain. If not provided, the source wallet&#39;s address will be used as the change address. | [optional] 
**validator_address** | **str** | The validator&#39;s EVM address. | 
**reward_address** | **str** | The EVM address to receive staking rewards. | 

## Example

```python
from cobo_waas2.models.create_stake_activity_extra import CreateStakeActivityExtra

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStakeActivityExtra from a JSON string
create_stake_activity_extra_instance = CreateStakeActivityExtra.from_json(json)
# print the JSON string representation of the object
print(CreateStakeActivityExtra.to_json())

# convert the object into a dict
create_stake_activity_extra_dict = create_stake_activity_extra_instance.to_dict()
# create an instance of CreateStakeActivityExtra from a dict
create_stake_activity_extra_from_dict = CreateStakeActivityExtra.from_dict(create_stake_activity_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


