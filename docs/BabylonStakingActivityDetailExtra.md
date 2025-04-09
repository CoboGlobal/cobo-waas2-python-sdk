# BabylonStakingActivityDetailExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**finality_provider_public_key** | **str** | The public key of the finality provider. | [optional] 
**stake_block_time** | **int** | The number of blocks that need to be processed before the locked tokens are unlocked and become accessible. | [optional] 
**auto_broadcast** | **bool** | Whether to automatically broadcast the transaction.  - &#x60;true&#x60;: Automatically broadcast the transaction. - &#x60;false&#x60;: The transaction will not be submitted to the blockchain automatically. You can call [Broadcast signed transactions](https://www.cobo.com/developers/v2/api-references/transactions/broadcast-signed-transactions) to broadcast the transaction to the blockchain, or retrieve the signed raw transaction data &#x60;raw_tx&#x60; by calling [Get transaction information](https://www.cobo.com/developers/v2/api-references/transactions/get-transaction-information) and broadcast it yourself.  | [optional] 

## Example

```python
from cobo_waas2.models.babylon_staking_activity_detail_extra import BabylonStakingActivityDetailExtra

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonStakingActivityDetailExtra from a JSON string
babylon_staking_activity_detail_extra_instance = BabylonStakingActivityDetailExtra.from_json(json)
# print the JSON string representation of the object
print(BabylonStakingActivityDetailExtra.to_json())

# convert the object into a dict
babylon_staking_activity_detail_extra_dict = babylon_staking_activity_detail_extra_instance.to_dict()
# create an instance of BabylonStakingActivityDetailExtra from a dict
babylon_staking_activity_detail_extra_from_dict = BabylonStakingActivityDetailExtra.from_dict(babylon_staking_activity_detail_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


