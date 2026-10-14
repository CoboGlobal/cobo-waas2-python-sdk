# TransactionSOLFee

The transaction fee actually charged by the chain that uses the Solana fee model.  For more details about the Solana fee model, see [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | A fixed fee, in lamports, charged per signature. The default is 5,000 per signature. | [optional] 
**rent_amount** | **str** | The one-time rent, in lamports, required to create the destination&#39;s Associated Token Account (ATA) for this token when it does not exist yet.  In fee estimate responses, this field returns the current on-chain rent if the destination address has no ATA for the token, and is empty otherwise. You can call [Estimate transaction fee](https://www.cobo.com/developers/v2/api-references/transactions/estimate-transaction-fee) before submitting a transaction to check whether it will incur ATA rent. The result reflects the destination at estimation time; if the ATA is closed before the transaction is built, the transaction still creates it and incurs the rent.  In transaction records, this field keeps the value estimated when the transaction was created and is not updated from on-chain data. &#x60;estimated_fee_used&#x60; includes this rent, while &#x60;fee_used&#x60; does not.  | [optional] 
**compute_unit_price** | **str** | The price paid per compute unit. This value determines the priority fee for the transaction, allowing you to increase inclusion probability in congested conditions. | [optional] 
**compute_unit_limit** | **str** | The maximum number of compute units your transaction is allowed to consume. It sets an upper bound on computational resource usage to prevent overload. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | [optional] 
**fee_used** | **str** | The actual on-chain network transaction fee charged for this Solana transaction. This covers the network fee only and does not include ATA activation rent. | [optional] 
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


