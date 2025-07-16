# EvmEip1559FeeBasePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_per_gas** | **str** | The maximum gas fee per gas unit used on the chain, in wei. | [optional] 
**max_priority_fee_per_gas** | **str** | The maximum priority fee per gas unit used, in wei. The maximum priority fee represents the highest amount of miner tips that you are willing to pay for your transaction. | [optional] 

## Example

```python
from cobo_waas2.models.evm_eip1559_fee_base_price import EvmEip1559FeeBasePrice

# TODO update the JSON string below
json = "{}"
# create an instance of EvmEip1559FeeBasePrice from a JSON string
evm_eip1559_fee_base_price_instance = EvmEip1559FeeBasePrice.from_json(json)
# print the JSON string representation of the object
print(EvmEip1559FeeBasePrice.to_json())

# convert the object into a dict
evm_eip1559_fee_base_price_dict = evm_eip1559_fee_base_price_instance.to_dict()
# create an instance of EvmEip1559FeeBasePrice from a dict
evm_eip1559_fee_base_price_from_dict = EvmEip1559FeeBasePrice.from_dict(evm_eip1559_fee_base_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


