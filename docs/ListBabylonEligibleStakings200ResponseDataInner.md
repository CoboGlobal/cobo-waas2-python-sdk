# ListBabylonEligibleStakings200ResponseDataInner

The babylon staking position eligible for post staking registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_id** | **str** | The unique identifier of the staking position | [optional] 
**btc_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**staked_amount** | **str** | Current staked amount in BTC | [optional] 
**status** | [**BabylonRegistrationStatus**](BabylonRegistrationStatus.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_babylon_eligible_stakings200_response_data_inner import ListBabylonEligibleStakings200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListBabylonEligibleStakings200ResponseDataInner from a JSON string
list_babylon_eligible_stakings200_response_data_inner_instance = ListBabylonEligibleStakings200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListBabylonEligibleStakings200ResponseDataInner.to_json())

# convert the object into a dict
list_babylon_eligible_stakings200_response_data_inner_dict = list_babylon_eligible_stakings200_response_data_inner_instance.to_dict()
# create an instance of ListBabylonEligibleStakings200ResponseDataInner from a dict
list_babylon_eligible_stakings200_response_data_inner_from_dict = ListBabylonEligibleStakings200ResponseDataInner.from_dict(list_babylon_eligible_stakings200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


