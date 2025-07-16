# EstimatedFILFee

The estimated transaction fee based on the fil fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 
**slow** | [**EstimatedFILFeeSlow**](EstimatedFILFeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedFILFeeSlow**](EstimatedFILFeeSlow.md) |  | 
**fast** | [**EstimatedFILFeeSlow**](EstimatedFILFeeSlow.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimated_fil_fee import EstimatedFILFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedFILFee from a JSON string
estimated_fil_fee_instance = EstimatedFILFee.from_json(json)
# print the JSON string representation of the object
print(EstimatedFILFee.to_json())

# convert the object into a dict
estimated_fil_fee_dict = estimated_fil_fee_instance.to_dict()
# create an instance of EstimatedFILFee from a dict
estimated_fil_fee_from_dict = EstimatedFILFee.from_dict(estimated_fil_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


