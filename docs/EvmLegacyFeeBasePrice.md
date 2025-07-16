# EvmLegacyFeeBasePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_price** | **str** | The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used. | [optional] 

## Example

```python
from cobo_waas2.models.evm_legacy_fee_base_price import EvmLegacyFeeBasePrice

# TODO update the JSON string below
json = "{}"
# create an instance of EvmLegacyFeeBasePrice from a JSON string
evm_legacy_fee_base_price_instance = EvmLegacyFeeBasePrice.from_json(json)
# print the JSON string representation of the object
print(EvmLegacyFeeBasePrice.to_json())

# convert the object into a dict
evm_legacy_fee_base_price_dict = evm_legacy_fee_base_price_instance.to_dict()
# create an instance of EvmLegacyFeeBasePrice from a dict
evm_legacy_fee_base_price_from_dict = EvmLegacyFeeBasePrice.from_dict(evm_legacy_fee_base_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


