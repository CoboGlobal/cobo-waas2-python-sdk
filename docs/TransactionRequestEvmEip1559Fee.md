# TransactionRequestEvmEip1559Fee

In the EIP-1559 fee model, the transaction fee is calculated by multiplying the gas price and the gas units used by the transaction. This can be expressed as: Transaction fee = gas price * gas units used.   You can specify the maximum gas fee per gas unit and the maximum priority fee per gas unit to limit the transaction fee amount. You can also specify the gas limit. If the gas units used exceeds the gas limit, the transaction will fail. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_per_gas** | **str** | The maximum gas fee per gas unit used on the chain, in wei. | 
**max_priority_fee_per_gas** | **str** | The maximum priority fee per gas unit used, in wei. The maximum priority fee represents the highest amount of miner tips that you are willing to pay for your transaction. | 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | [optional] [default to '21000']

## Example

```python
from cobo_waas2.models.transaction_request_evm_eip1559_fee import TransactionRequestEvmEip1559Fee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestEvmEip1559Fee from a JSON string
transaction_request_evm_eip1559_fee_instance = TransactionRequestEvmEip1559Fee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestEvmEip1559Fee.to_json())

# convert the object into a dict
transaction_request_evm_eip1559_fee_dict = transaction_request_evm_eip1559_fee_instance.to_dict()
# create an instance of TransactionRequestEvmEip1559Fee from a dict
transaction_request_evm_eip1559_fee_from_dict = TransactionRequestEvmEip1559Fee.from_dict(transaction_request_evm_eip1559_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


