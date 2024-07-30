# EstimatedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**is_loop** | **bool** | Whether the transaction can be executed as a Loop transfer. For more information about Loop, see [Loop&#39;s website](https://loop.top/). - &#x60;true&#x60;: The transaction is a Loop transfer. - &#x60;false&#x60;: The transaction is not a Loop transfer.  | [optional] 
**fee_amount** | **str** | The fee that you need to pay for the transaction. | 
**slow** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | 
**fast** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.estimated_fee import EstimatedFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedFee from a JSON string
estimated_fee_instance = EstimatedFee.from_json(json)
# print the JSON string representation of the object
print(EstimatedFee.to_json())

# convert the object into a dict
estimated_fee_dict = estimated_fee_instance.to_dict()
# create an instance of EstimatedFee from a dict
estimated_fee_from_dict = EstimatedFee.from_dict(estimated_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


