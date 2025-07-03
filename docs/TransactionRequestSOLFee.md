# TransactionRequestSOLFee

The preset properties to limit transaction fee.  In the SOL fee model, the calculation method for the fee is: fee = base_fee + compute_unit_price * compute_unit_limit + rent_amount, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  You can specify the compute_unit_price, compute_unit_limit.   Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_unit_price** | **str** | The cost per compute unit. Transactions consume computational resources measured in compute units, and this price helps determine the cost of executing transactions, especially complex ones involving smart contracts. | 
**compute_unit_limit** | **str** | The maximum number of compute units allowed for a transaction. This limits the resources any single transaction can consume, preventing excessive resource usage that could impact network performance negatively. | 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 

## Example

```python
from cobo_waas2.models.transaction_request_sol_fee import TransactionRequestSOLFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestSOLFee from a JSON string
transaction_request_sol_fee_instance = TransactionRequestSOLFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestSOLFee.to_json())

# convert the object into a dict
transaction_request_sol_fee_dict = transaction_request_sol_fee_instance.to_dict()
# create an instance of TransactionRequestSOLFee from a dict
transaction_request_sol_fee_from_dict = TransactionRequestSOLFee.from_dict(transaction_request_sol_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


