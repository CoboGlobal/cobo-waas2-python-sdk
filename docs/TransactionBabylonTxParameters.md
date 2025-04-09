# TransactionBabylonTxParameters

The Babylon transaction parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_type** | [**TransactionExtraType**](TransactionExtraType.md) |  | 
**stake_amount** | **str** | The origin staking amount. | [optional] 
**finality_provider_public_key** | **str** | The public key of the finality provider. | [optional] 
**stake_block_time** | **int** | The number of blocks that need to be processed before the locked tokens are unlocked and become accessible. | [optional] 
**param_version** | **int** | The version of babylon global parameters. | [optional] 
**withdraw_from_type** | [**ActivityType**](ActivityType.md) |  | [optional] 
**slash_from_type** | [**ActivityType**](ActivityType.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_babylon_tx_parameters import TransactionBabylonTxParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionBabylonTxParameters from a JSON string
transaction_babylon_tx_parameters_instance = TransactionBabylonTxParameters.from_json(json)
# print the JSON string representation of the object
print(TransactionBabylonTxParameters.to_json())

# convert the object into a dict
transaction_babylon_tx_parameters_dict = transaction_babylon_tx_parameters_instance.to_dict()
# create an instance of TransactionBabylonTxParameters from a dict
transaction_babylon_tx_parameters_from_dict = TransactionBabylonTxParameters.from_dict(transaction_babylon_tx_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


