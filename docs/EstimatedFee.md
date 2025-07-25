# EstimatedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 
**is_loop** | **bool** | Whether the transaction was executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer. - &#x60;true&#x60;: The transaction was executed as a Cobo Loop transfer. - &#x60;false&#x60;: The transaction was not executed as a Cobo Loop transfer.  | [optional] 
**fee_amount** | **str** | The transaction fee that you need to pay for the transaction. | 
**slow** | [**EstimatedFILFeeSlow**](EstimatedFILFeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedFILFeeSlow**](EstimatedFILFeeSlow.md) |  | 
**fast** | [**EstimatedFILFeeSlow**](EstimatedFILFeeSlow.md) |  | [optional] 

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


