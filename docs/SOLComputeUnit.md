# SOLComputeUnit

The transaction gas price based on the SOL fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_unit_price** | **str** | The cost per compute unit. Transactions consume computational resources measured in compute units, and this price helps determine the cost of executing transactions, especially complex ones involving smart contracts. | [optional] 
**compute_unit_limit** | **str** | The maximum number of compute units allowed for a transaction. This limits the resources any single transaction can consume, preventing excessive resource usage that could impact network performance negatively. | [optional] 

## Example

```python
from cobo_waas2.models.sol_compute_unit import SOLComputeUnit

# TODO update the JSON string below
json = "{}"
# create an instance of SOLComputeUnit from a JSON string
sol_compute_unit_instance = SOLComputeUnit.from_json(json)
# print the JSON string representation of the object
print(SOLComputeUnit.to_json())

# convert the object into a dict
sol_compute_unit_dict = sol_compute_unit_instance.to_dict()
# create an instance of SOLComputeUnit from a dict
sol_compute_unit_from_dict = SOLComputeUnit.from_dict(sol_compute_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


