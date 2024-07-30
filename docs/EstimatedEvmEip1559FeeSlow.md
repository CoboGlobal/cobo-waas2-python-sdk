# EstimatedEvmEip1559FeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_per_gas** | **str** | The maximum gas fee per gas unit used on the chain, in wei. | 
**max_priority_fee_per_gas** | **str** | The maximum priority fee per gas unit used, in wei. The maximum priority fee represents the highest amount of miner tips that you are willing to pay for your transaction. | 
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | [default to '21000']

## Example

```python
from cobo_waas2.models.estimated_evm_eip1559_fee_slow import EstimatedEvmEip1559FeeSlow

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedEvmEip1559FeeSlow from a JSON string
estimated_evm_eip1559_fee_slow_instance = EstimatedEvmEip1559FeeSlow.from_json(json)
# print the JSON string representation of the object
print(EstimatedEvmEip1559FeeSlow.to_json())

# convert the object into a dict
estimated_evm_eip1559_fee_slow_dict = estimated_evm_eip1559_fee_slow_instance.to_dict()
# create an instance of EstimatedEvmEip1559FeeSlow from a dict
estimated_evm_eip1559_fee_slow_from_dict = EstimatedEvmEip1559FeeSlow.from_dict(estimated_evm_eip1559_fee_slow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


