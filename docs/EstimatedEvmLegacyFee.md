# EstimatedEvmLegacyFee

The estimated transaction fee based on the legacy fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**slow** | [**EstimatedEvmLegacyFeeSlow**](EstimatedEvmLegacyFeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedEvmLegacyFeeSlow**](EstimatedEvmLegacyFeeSlow.md) |  | 
**fast** | [**EstimatedEvmLegacyFeeSlow**](EstimatedEvmLegacyFeeSlow.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimated_evm_legacy_fee import EstimatedEvmLegacyFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedEvmLegacyFee from a JSON string
estimated_evm_legacy_fee_instance = EstimatedEvmLegacyFee.from_json(json)
# print the JSON string representation of the object
print(EstimatedEvmLegacyFee.to_json())

# convert the object into a dict
estimated_evm_legacy_fee_dict = estimated_evm_legacy_fee_instance.to_dict()
# create an instance of EstimatedEvmLegacyFee from a dict
estimated_evm_legacy_fee_from_dict = EstimatedEvmLegacyFee.from_dict(estimated_evm_legacy_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


