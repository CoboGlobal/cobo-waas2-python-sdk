# TransactionExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_type** | [**TransactionExtraType**](TransactionExtraType.md) |  | 
**babylon_address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**btc_address_info** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**stake_amount** | **str** | The origin staking amount. | [optional] 
**finality_provider_public_key** | **str** | The public key of the finality provider. | [optional] 
**stake_block_time** | **int** | The number of blocks that need to be processed before the locked tokens are unlocked and become accessible. | [optional] 
**param_version** | **int** | The version of babylon global parameters. | [optional] 
**withdraw_from_type** | [**ActivityType**](ActivityType.md) |  | [optional] 
**slash_from_type** | [**ActivityType**](ActivityType.md) |  | [optional] 
**timelock** | **int** | The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal. | [optional] 
**change_address** | **str** | The change address on the Bitcoin chain. If not provided, the source wallet&#39;s address will be used as the change address. | [optional] 
**validator_address** | **str** | The validator&#39;s EVM address. | [optional] 
**reward_address** | **str** | The EVM address to receive staking rewards. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_extra import TransactionExtra

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionExtra from a JSON string
transaction_extra_instance = TransactionExtra.from_json(json)
# print the JSON string representation of the object
print(TransactionExtra.to_json())

# convert the object into a dict
transaction_extra_dict = transaction_extra_instance.to_dict()
# create an instance of TransactionExtra from a dict
transaction_extra_from_dict = TransactionExtra.from_dict(transaction_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


