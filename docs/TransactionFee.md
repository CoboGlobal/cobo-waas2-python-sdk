# TransactionFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | [optional] 
**effective_gas_price** | **str** | The gas price (gas fee per gas unit) on the chain, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions. | [optional] 
**fee_used** | **str** | The actually charged transaction fee. | [optional] 
**estimated_fee_used** | **str** | The estimated transaction fee. | [optional] 
**gas_used** | **str** | The gas units used in the transaction. | [optional] 
**max_fee_per_gas** | **str** | The maximum gas fee per gas unit used on the chain, in wei. | [optional] 
**max_priority_fee_per_gas** | **str** | The maximum priority fee per gas unit used, in wei. The maximum priority fee represents the highest amount of miner tips that you are willing to pay for your transaction. | [optional] 
**gas_limit** | **str** | The maximum amount of gas your transaction is allowed to consume. | [optional] 
**gas_price** | **str** | The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used. | [optional] 
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. Provide the value without applying precision. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | [optional] 
**base_fee** | **str** | A fixed fee, in lamports, charged per signature. The default is 5,000 per signature. | [optional] 
**rent_amount** | **str** | The one-time rent, in lamports, required to create the destination&#39;s Associated Token Account (ATA) for this token when it does not exist yet.  In fee estimate responses, this field returns the current on-chain rent if the destination address has no ATA for the token, and is empty otherwise. You can call [Estimate transaction fee](https://www.cobo.com/developers/v2/api-references/transactions/estimate-transaction-fee) before submitting a transaction to check whether it will incur ATA rent. The result reflects the destination at estimation time; if the ATA is closed before the transaction is built, the transaction still creates it and incurs the rent.  In transaction records, this field keeps the value estimated when the transaction was created and is not updated from on-chain data. &#x60;estimated_fee_used&#x60; includes this rent, while &#x60;fee_used&#x60; does not.  | [optional] 
**compute_unit_price** | **str** | The price paid per compute unit. This value determines the priority fee for the transaction, allowing you to increase inclusion probability in congested conditions. | [optional] 
**compute_unit_limit** | **str** | The maximum number of compute units your transaction is allowed to consume. It sets an upper bound on computational resource usage to prevent overload. | [optional] 
**gas_base** | **str** | This is the minimum fee required to include a transaction in a block. It is determined by the network&#39;s congestion level, which adjusts to maintain a target block utilization rate. The base fee is burned, reducing the total supply of Filecoin over time. | [optional] 
**gas_premium** | **str** | An optional additional fee that users can include to prioritize their transactions over others. It acts like a tip to incentivize miners to select and include your transaction over transactions with only the base fee. | [optional] 
**gas_fee_cap** | **str** | The gas_fee_cap is a user-defined limit on how much they are willing to pay per unit of gas. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_fee import TransactionFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFee from a JSON string
transaction_fee_instance = TransactionFee.from_json(json)
# print the JSON string representation of the object
print(TransactionFee.to_json())

# convert the object into a dict
transaction_fee_dict = transaction_fee_instance.to_dict()
# create an instance of TransactionFee from a dict
transaction_fee_from_dict = TransactionFee.from_dict(transaction_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


