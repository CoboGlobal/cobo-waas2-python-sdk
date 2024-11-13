# FeeGasLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | [optional] 

## Example

```python
from cobo_waas2.models.fee_gas_limit import FeeGasLimit

# TODO update the JSON string below
json = "{}"
# create an instance of FeeGasLimit from a JSON string
fee_gas_limit_instance = FeeGasLimit.from_json(json)
# print the JSON string representation of the object
print(FeeGasLimit.to_json())

# convert the object into a dict
fee_gas_limit_dict = fee_gas_limit_instance.to_dict()
# create an instance of FeeGasLimit from a dict
fee_gas_limit_from_dict = FeeGasLimit.from_dict(fee_gas_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


