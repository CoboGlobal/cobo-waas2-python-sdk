# FeeRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 
**fee_amount** | **str** | The transaction fee that you need to pay for the transaction. | [optional] 
**slow** | [**UtxoFeeBasePrice**](UtxoFeeBasePrice.md) |  | [optional] 
**recommended** | [**UtxoFeeBasePrice**](UtxoFeeBasePrice.md) |  | 
**fast** | [**UtxoFeeBasePrice**](UtxoFeeBasePrice.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.fee_rate import FeeRate

# TODO update the JSON string below
json = "{}"
# create an instance of FeeRate from a JSON string
fee_rate_instance = FeeRate.from_json(json)
# print the JSON string representation of the object
print(FeeRate.to_json())

# convert the object into a dict
fee_rate_dict = fee_rate_instance.to_dict()
# create an instance of FeeRate from a dict
fee_rate_from_dict = FeeRate.from_dict(fee_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


