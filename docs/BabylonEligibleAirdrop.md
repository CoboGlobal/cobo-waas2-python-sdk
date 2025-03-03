# BabylonEligibleAirdrop

The babylon airdrop eligibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**babylon_points** | **str** | The current Babylon points balance accumulated by the BTC address. | [optional] 
**airdrop_amount** | **str** | The estimated airdrop amount based on the current Babylon points balance. | [optional] 
**status** | [**BabylonRegistrationStatus**](BabylonRegistrationStatus.md) |  | [optional] 
**pop** | [**BabylonAirdropPop**](BabylonAirdropPop.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.babylon_eligible_airdrop import BabylonEligibleAirdrop

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonEligibleAirdrop from a JSON string
babylon_eligible_airdrop_instance = BabylonEligibleAirdrop.from_json(json)
# print the JSON string representation of the object
print(BabylonEligibleAirdrop.to_json())

# convert the object into a dict
babylon_eligible_airdrop_dict = babylon_eligible_airdrop_instance.to_dict()
# create an instance of BabylonEligibleAirdrop from a dict
babylon_eligible_airdrop_from_dict = BabylonEligibleAirdrop.from_dict(babylon_eligible_airdrop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


