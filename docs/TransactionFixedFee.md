# TransactionFixedFee

The transaction fee actually charged by the chain that uses the fixed fee model.   Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. Provide the value without applying precision. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | [optional] 
**fee_used** | **str** | The actually charged transaction fee. | [optional] 
**estimated_fee_used** | **str** | The estimated transaction fee. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_fixed_fee import TransactionFixedFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFixedFee from a JSON string
transaction_fixed_fee_instance = TransactionFixedFee.from_json(json)
# print the JSON string representation of the object
print(TransactionFixedFee.to_json())

# convert the object into a dict
transaction_fixed_fee_dict = transaction_fixed_fee_instance.to_dict()
# create an instance of TransactionFixedFee from a dict
transaction_fixed_fee_from_dict = TransactionFixedFee.from_dict(transaction_fixed_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


