# EstimatedEvmLegacyFeeSlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_price** | **str** | The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used. | 
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | 

## Example

```python
from cobo_waas2.models.estimated_evm_legacy_fee_slow import EstimatedEvmLegacyFeeSlow

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedEvmLegacyFeeSlow from a JSON string
estimated_evm_legacy_fee_slow_instance = EstimatedEvmLegacyFeeSlow.from_json(json)
# print the JSON string representation of the object
print(EstimatedEvmLegacyFeeSlow.to_json())

# convert the object into a dict
estimated_evm_legacy_fee_slow_dict = estimated_evm_legacy_fee_slow_instance.to_dict()
# create an instance of EstimatedEvmLegacyFeeSlow from a dict
estimated_evm_legacy_fee_slow_from_dict = EstimatedEvmLegacyFeeSlow.from_dict(estimated_evm_legacy_fee_slow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


