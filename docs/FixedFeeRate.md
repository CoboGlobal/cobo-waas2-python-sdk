# FixedFeeRate

The transaction fee that you need to pay based on the fixed fee model for some blockchains. The fee can vary between different chains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | **str** | The transaction fee that you need to pay for the transaction. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 

## Example

```python
from cobo_waas2.models.fixed_fee_rate import FixedFeeRate

# TODO update the JSON string below
json = "{}"
# create an instance of FixedFeeRate from a JSON string
fixed_fee_rate_instance = FixedFeeRate.from_json(json)
# print the JSON string representation of the object
print(FixedFeeRate.to_json())

# convert the object into a dict
fixed_fee_rate_dict = fixed_fee_rate_instance.to_dict()
# create an instance of FixedFeeRate from a dict
fixed_fee_rate_from_dict = FixedFeeRate.from_dict(fixed_fee_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


