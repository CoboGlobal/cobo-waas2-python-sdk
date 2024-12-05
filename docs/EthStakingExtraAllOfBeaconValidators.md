# EthStakingExtraAllOfBeaconValidators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | The validator public key. | [optional] 
**status** | [**AmountStatus**](AmountStatus.md) |  | [optional] 
**apy** | **float** | The annual percentage yield (APY) of the validator. | [optional] 
**staked_amount** | **str** | The staked amount. | [optional] 
**rewards_received** | **str** | The rewards received. | [optional] 
**updated_timestamp** | **int** | The updated timestamp. | [optional] 

## Example

```python
from cobo_waas2.models.eth_staking_extra_all_of_beacon_validators import EthStakingExtraAllOfBeaconValidators

# TODO update the JSON string below
json = "{}"
# create an instance of EthStakingExtraAllOfBeaconValidators from a JSON string
eth_staking_extra_all_of_beacon_validators_instance = EthStakingExtraAllOfBeaconValidators.from_json(json)
# print the JSON string representation of the object
print(EthStakingExtraAllOfBeaconValidators.to_json())

# convert the object into a dict
eth_staking_extra_all_of_beacon_validators_dict = eth_staking_extra_all_of_beacon_validators_instance.to_dict()
# create an instance of EthStakingExtraAllOfBeaconValidators from a dict
eth_staking_extra_all_of_beacon_validators_from_dict = EthStakingExtraAllOfBeaconValidators.from_dict(eth_staking_extra_all_of_beacon_validators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


