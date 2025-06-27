# EstimatedSOLFee

The estimated transaction fee based on the sol fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**slow** | [**EstimatedSOLFeeSlow**](EstimatedSOLFeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedSOLFeeSlow**](EstimatedSOLFeeSlow.md) |  | 
**fast** | [**EstimatedSOLFeeSlow**](EstimatedSOLFeeSlow.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimated_sol_fee import EstimatedSOLFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedSOLFee from a JSON string
estimated_sol_fee_instance = EstimatedSOLFee.from_json(json)
# print the JSON string representation of the object
print(EstimatedSOLFee.to_json())

# convert the object into a dict
estimated_sol_fee_dict = estimated_sol_fee_instance.to_dict()
# create an instance of EstimatedSOLFee from a dict
estimated_sol_fee_from_dict = EstimatedSOLFee.from_dict(estimated_sol_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


