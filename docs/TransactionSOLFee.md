# TransactionSOLFee

The transaction fee actually charged by the chain that uses the Solana fee model.  In this model, the fee is calculated as: fee = base fee + (compute unit price * compute unit limit) + rent (if applicable). For more details, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | A fixed fee charged per signature. The default is 5,000 lamports per signature. | [optional] 
**rent_amount** | **str** | The rent fee charged by the network to store non–rent-exempt accounts on-chain. It is deducted periodically until the account maintains the minimum balance required for rent exemption. | [optional] 
**compute_unit_price** | **str** | The price paid per compute unit. This value determines the priority fee for the transaction, allowing you to increase inclusion probability in congested conditions. | [optional] 
**compute_unit_limit** | **str** | The maximum number of compute units your transaction is allowed to consume. It sets an upper bound on computational resource usage to prevent overload. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | [optional] 
**fee_used** | **str** | The actually charged transaction fee. | [optional] 
**estimated_fee_used** | **str** | The estimated transaction fee. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_sol_fee import TransactionSOLFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSOLFee from a JSON string
transaction_sol_fee_instance = TransactionSOLFee.from_json(json)
# print the JSON string representation of the object
print(TransactionSOLFee.to_json())

# convert the object into a dict
transaction_sol_fee_dict = transaction_sol_fee_instance.to_dict()
# create an instance of TransactionSOLFee from a dict
transaction_sol_fee_from_dict = TransactionSOLFee.from_dict(transaction_sol_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


