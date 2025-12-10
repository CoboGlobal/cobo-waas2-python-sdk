# PayoutEstimatedFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**is_loop** | **bool** | Whether the transaction was executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer. - &#x60;true&#x60;: The transaction was executed as a Cobo Loop transfer. - &#x60;false&#x60;: The transaction was not executed as a Cobo Loop transfer.  | [optional] 
**fee_amount** | **str** | The transaction fee that you need to pay for the transaction. | 
**slow** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | [optional] 
**recommended** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | 
**fast** | [**EstimatedUtxoFeeSlow**](EstimatedUtxoFeeSlow.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payout_estimated_fee import PayoutEstimatedFee

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutEstimatedFee from a JSON string
payout_estimated_fee_instance = PayoutEstimatedFee.from_json(json)
# print the JSON string representation of the object
print(PayoutEstimatedFee.to_json())

# convert the object into a dict
payout_estimated_fee_dict = payout_estimated_fee_instance.to_dict()
# create an instance of PayoutEstimatedFee from a dict
payout_estimated_fee_from_dict = PayoutEstimatedFee.from_dict(payout_estimated_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


