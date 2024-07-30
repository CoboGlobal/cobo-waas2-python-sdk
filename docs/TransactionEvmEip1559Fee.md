# TransactionEvmEip1559Fee

The transaction fee actually charged by the chain that uses the EIP-1559 fee model.  The transaction fee is calculated by multiplying the gas price by the used gas units. This can be expressed as: Transaction fee = gas price * used gas units. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_per_gas** | **str** | The maximum gas fee per gas unit used on the chain, in wei. | [optional] 
**max_priority_fee_per_gas** | **str** | The maximum priority fee per gas unit used, in wei. The maximum priority fee represents the highest amount of miner tips that you are willing to pay for your transaction. | [optional] 
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | [optional] [default to '21000']
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | [optional] 
**effective_gas_price** | **str** | The gas price (gas fee per gas unit) on the chain, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions. | [optional] 
**fee_used** | **str** | The transaction fee. | [optional] 
**gas_used** | **str** | The number of gas units used in the transaction. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_evm_eip1559_fee import TransactionEvmEip1559Fee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEvmEip1559Fee from a JSON string
transaction_evm_eip1559_fee_instance = TransactionEvmEip1559Fee.from_json(json)
# print the JSON string representation of the object
print(TransactionEvmEip1559Fee.to_json())

# convert the object into a dict
transaction_evm_eip1559_fee_dict = transaction_evm_eip1559_fee_instance.to_dict()
# create an instance of TransactionEvmEip1559Fee from a dict
transaction_evm_eip1559_fee_from_dict = TransactionEvmEip1559Fee.from_dict(transaction_evm_eip1559_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


