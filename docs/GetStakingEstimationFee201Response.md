# GetStakingEstimationFee201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | [optional] 
**fee** | [**EstimatedFee**](EstimatedFee.md) |  | [optional] 
**validator_pubkeys** | **List[str]** | A list of public keys associated with the Ethereum validators for this staking operation. | [optional] 
**core_btc_staking_address** | **str** | P2WSH address generated for this staking operation(If the estimated fee is for core BTC staking). | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | [optional] 
**fee_amount** | **str** | The amount of the estimated fee. | [optional] 
**token_id** | **str** | The token ID of the staking fee. | [optional] 

## Example

```python
from cobo_waas2.models.get_staking_estimation_fee201_response import GetStakingEstimationFee201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStakingEstimationFee201Response from a JSON string
get_staking_estimation_fee201_response_instance = GetStakingEstimationFee201Response.from_json(json)
# print the JSON string representation of the object
print(GetStakingEstimationFee201Response.to_json())

# convert the object into a dict
get_staking_estimation_fee201_response_dict = get_staking_estimation_fee201_response_instance.to_dict()
# create an instance of GetStakingEstimationFee201Response from a dict
get_staking_estimation_fee201_response_from_dict = GetStakingEstimationFee201Response.from_dict(get_staking_estimation_fee201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


