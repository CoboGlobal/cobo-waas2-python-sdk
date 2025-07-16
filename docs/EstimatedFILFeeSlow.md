# EstimatedFILFeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_premium** | **str** | An optional tip you can include to prioritize your transaction. The gas premium incentivizes miners to include your transaction sooner than those offering only the base fee. | 
**gas_fee_cap** | **str** | The maximum gas price you are willing to pay per unit of gas. | 
**gas_limit** | **str** | The maximum amount of gas your transaction is allowed to consume. | 
**gas_base** | **str** | The minimum fee required for a transaction to be included in a block. The base fee is dynamically adjusted based on network congestion to maintain target block utilization. It is burned rather than paid to miners, reducing the total Filecoin supply over time. | 

## Example

```python
from cobo_waas2.models.estimated_fil_fee_slow import EstimatedFILFeeSlow

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedFILFeeSlow from a JSON string
estimated_fil_fee_slow_instance = EstimatedFILFeeSlow.from_json(json)
# print the JSON string representation of the object
print(EstimatedFILFeeSlow.to_json())

# convert the object into a dict
estimated_fil_fee_slow_dict = estimated_fil_fee_slow_instance.to_dict()
# create an instance of EstimatedFILFeeSlow from a dict
estimated_fil_fee_slow_from_dict = EstimatedFILFeeSlow.from_dict(estimated_fil_fee_slow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


