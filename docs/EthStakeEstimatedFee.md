# EthStakeEstimatedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | [optional] 
**fee** | [**EstimatedFee**](EstimatedFee.md) |  | [optional] 
**validator_pubkeys** | **List[str]** | A list of public keys associated with the Ethereum validators for this staking operation. | [optional] 
**core_btc_staking_address** | **str** | P2WSH address generated for this staking operation(If the estimated fee is for core BTC staking). | [optional] 

## Example

```python
from cobo_waas2.models.eth_stake_estimated_fee import EthStakeEstimatedFee

# TODO update the JSON string below
json = "{}"
# create an instance of EthStakeEstimatedFee from a JSON string
eth_stake_estimated_fee_instance = EthStakeEstimatedFee.from_json(json)
# print the JSON string representation of the object
print(EthStakeEstimatedFee.to_json())

# convert the object into a dict
eth_stake_estimated_fee_dict = eth_stake_estimated_fee_instance.to_dict()
# create an instance of EthStakeEstimatedFee from a dict
eth_stake_estimated_fee_from_dict = EthStakeEstimatedFee.from_dict(eth_stake_estimated_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


