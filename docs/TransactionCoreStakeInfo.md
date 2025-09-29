# TransactionCoreStakeInfo

The core stake information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_type** | [**TransactionExtraType**](TransactionExtraType.md) |  | 
**stake_amount** | **str** | The origin staking amount. | [optional] 
**timelock** | **int** | The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal. | [optional] 
**change_address** | **str** | The change address on the Bitcoin chain. If not provided, the source wallet&#39;s address will be used as the change address. | [optional] 
**validator_address** | **str** | The validator&#39;s EVM address. | [optional] 
**reward_address** | **str** | The EVM address to receive staking rewards. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_core_stake_info import TransactionCoreStakeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCoreStakeInfo from a JSON string
transaction_core_stake_info_instance = TransactionCoreStakeInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionCoreStakeInfo.to_json())

# convert the object into a dict
transaction_core_stake_info_dict = transaction_core_stake_info_instance.to_dict()
# create an instance of TransactionCoreStakeInfo from a dict
transaction_core_stake_info_from_dict = TransactionCoreStakeInfo.from_dict(transaction_core_stake_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


