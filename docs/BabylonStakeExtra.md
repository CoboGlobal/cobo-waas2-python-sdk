# BabylonStakeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**finality_provider_public_key** | **str** | The public key of the finality provider. | 
**stake_block_time** | **int** | The number of blocks that need to be processed before the locked tokens are unlocked and become accessible. | 
**auto_broadcast** | **bool** | Whether to automatically broadcast the transaction. The default value is &#x60;true&#x60;.  - &#x60;true&#x60;: Automatically broadcast the transaction. - &#x60;false&#x60;: The transaction will not be submitted to the blockchain automatically. You can call [Broadcast signed transactions](https://www.cobo.com/developers/v2/api-references/transactions/broadcast-signed-transactions) to broadcast the transaction to the blockchain, or retrieve the signed raw transaction data &#x60;raw_tx&#x60; by calling [Get transaction information](https://www.cobo.com/developers/v2/api-references/transactions/get-transaction-information) and broadcast it yourself.  | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.babylon_stake_extra import BabylonStakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonStakeExtra from a JSON string
babylon_stake_extra_instance = BabylonStakeExtra.from_json(json)
# print the JSON string representation of the object
print(BabylonStakeExtra.to_json())

# convert the object into a dict
babylon_stake_extra_dict = babylon_stake_extra_instance.to_dict()
# create an instance of BabylonStakeExtra from a dict
babylon_stake_extra_from_dict = BabylonStakeExtra.from_dict(babylon_stake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


