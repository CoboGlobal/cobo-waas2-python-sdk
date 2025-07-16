# EvmEip1559FeeRate

The transaction fee rate based on the EIP-1559 fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 
**slow** | [**EvmEip1559FeeBasePrice**](EvmEip1559FeeBasePrice.md) |  | [optional] 
**recommended** | [**EvmEip1559FeeBasePrice**](EvmEip1559FeeBasePrice.md) |  | 
**fast** | [**EvmEip1559FeeBasePrice**](EvmEip1559FeeBasePrice.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.evm_eip1559_fee_rate import EvmEip1559FeeRate

# TODO update the JSON string below
json = "{}"
# create an instance of EvmEip1559FeeRate from a JSON string
evm_eip1559_fee_rate_instance = EvmEip1559FeeRate.from_json(json)
# print the JSON string representation of the object
print(EvmEip1559FeeRate.to_json())

# convert the object into a dict
evm_eip1559_fee_rate_dict = evm_eip1559_fee_rate_instance.to_dict()
# create an instance of EvmEip1559FeeRate from a dict
evm_eip1559_fee_rate_from_dict = EvmEip1559FeeRate.from_dict(evm_eip1559_fee_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


