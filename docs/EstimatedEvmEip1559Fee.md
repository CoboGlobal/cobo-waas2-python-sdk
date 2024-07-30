# EstimatedEvmEip1559Fee

The estimated transaction fee based on the EIP-1559 fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**slow** | [**EstimatedEvmEip1559FeeSlow**](EstimatedEvmEip1559FeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedEvmEip1559FeeSlow**](EstimatedEvmEip1559FeeSlow.md) |  | 
**fast** | [**EstimatedEvmEip1559FeeSlow**](EstimatedEvmEip1559FeeSlow.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimated_evm_eip1559_fee import EstimatedEvmEip1559Fee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedEvmEip1559Fee from a JSON string
estimated_evm_eip1559_fee_instance = EstimatedEvmEip1559Fee.from_json(json)
# print the JSON string representation of the object
print(EstimatedEvmEip1559Fee.to_json())

# convert the object into a dict
estimated_evm_eip1559_fee_dict = estimated_evm_eip1559_fee_instance.to_dict()
# create an instance of EstimatedEvmEip1559Fee from a dict
estimated_evm_eip1559_fee_from_dict = EstimatedEvmEip1559Fee.from_dict(estimated_evm_eip1559_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


