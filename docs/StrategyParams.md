# StrategyParams

Strategy parameters for commission calculation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bps** | **str** | Basis points | [optional] 
**min_fee** | **str** | Minimum fee | [optional] 
**additional_fixed_fee** | **str** | Additional fixed fee | [optional] 

## Example

```python
from cobo_waas2.models.strategy_params import StrategyParams

# TODO update the JSON string below
json = "{}"
# create an instance of StrategyParams from a JSON string
strategy_params_instance = StrategyParams.from_json(json)
# print the JSON string representation of the object
print(StrategyParams.to_json())

# convert the object into a dict
strategy_params_dict = strategy_params_instance.to_dict()
# create an instance of StrategyParams from a dict
strategy_params_from_dict = StrategyParams.from_dict(strategy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


