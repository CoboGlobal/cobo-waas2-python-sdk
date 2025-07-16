# TransactionRequestSOLFee

The preset properties to limit transaction fee.  In the Solana fee model, the transaction fee is calculated by adding the base fee to the product of the compute unit limit and the compute unit price. This can be expressed as: Transaction fee = base fee + (CU limit * CU price). For more information about the Solana fee model, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  You can specify CU price and CU limit to adjust the priority and resource allocation of your transaction.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_unit_price** | **str** | The price paid per compute unit. This value determines the priority fee for the transaction, allowing you to increase inclusion probability in congested conditions. | 
**compute_unit_limit** | **str** | The maximum number of compute units your transaction is allowed to consume. It sets an upper bound on computational resource usage to prevent overload. | 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 

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


