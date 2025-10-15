# EstimatedFixedFee

The estimated transaction fee based on the fixed fee model.  For more details about the fixed fee model, see [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | **str** | The transaction fee that you need to pay for the transaction. | 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 
**is_loop** | **bool** | Whether the transaction was executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer. - &#x60;true&#x60;: The transaction was executed as a Cobo Loop transfer. - &#x60;false&#x60;: The transaction was not executed as a Cobo Loop transfer.  | [optional] 

## Example

```python
from cobo_waas2.models.estimated_fixed_fee import EstimatedFixedFee

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedFixedFee from a JSON string
estimated_fixed_fee_instance = EstimatedFixedFee.from_json(json)
# print the JSON string representation of the object
print(EstimatedFixedFee.to_json())

# convert the object into a dict
estimated_fixed_fee_dict = estimated_fixed_fee_instance.to_dict()
# create an instance of EstimatedFixedFee from a dict
estimated_fixed_fee_from_dict = EstimatedFixedFee.from_dict(estimated_fixed_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


