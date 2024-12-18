# TransactionRequestFixedFee

The preset properties to limit transaction fee.  In the fixed fee model, the transaction fee is a fixed amount within a certain amount of period regardless of the transaction size or network congestion, which can vary between different chains. For more information about the fixed fee model, refer to [Fee models](/v2/guides/transactions/estimate-fees#fee-models).  You can specify the maximum fee amount to limit the transaction fee. The transaction will fail if the transaction fee exceeds the specified maximum fee amount.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 

## Example

```python
from cobo_waas2.models.transaction_request_fixed_fee import TransactionRequestFixedFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestFixedFee from a JSON string
transaction_request_fixed_fee_instance = TransactionRequestFixedFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestFixedFee.to_json())

# convert the object into a dict
transaction_request_fixed_fee_dict = transaction_request_fixed_fee_instance.to_dict()
# create an instance of TransactionRequestFixedFee from a dict
transaction_request_fixed_fee_from_dict = TransactionRequestFixedFee.from_dict(transaction_request_fixed_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


