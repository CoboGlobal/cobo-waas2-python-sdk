# TransactionReceipt

The information about a transaction receipt, which records the execution result of a transaction that has been included in a block.  All the numeric properties are returned as decimal values instead of the hexadecimal values used by the JSON-RPC interfaces of the chains. The properties that record on-chain amounts are returned as strings to avoid any precision loss. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
**transaction_hash** | **str** | The transaction hash, returned with the &#x60;0x&#x60; prefix. | 
**status** | **int** | The execution result of the transaction. - &#x60;1&#x60;: The transaction was executed successfully. - &#x60;0&#x60;: The transaction failed, for example, because it was reverted by the contract or ran out of gas.  | 
**block_number** | **int** | The number of the block that contains the transaction. | 
**block_hash** | **str** | The hash of the block that contains the transaction. | 
**transaction_index** | **int** | The index position of the transaction within the block. | 
**from_address** | **str** | The address that sent the transaction. | 
**to_address** | **str** | The address that received the transaction. The value is &#x60;null&#x60; if the transaction created a contract. | [optional] 
**contract_address** | **str** | The address of the contract created by the transaction. The value is &#x60;null&#x60; if the transaction did not create a contract. | [optional] 
**gas_used** | **str** | The number of gas units consumed by the transaction. | 
**cumulative_gas_used** | **str** | The total number of gas units consumed by all the transactions up to and including this transaction in the block. | [optional] 
**effective_gas_price** | **str** | The gas price actually paid for each gas unit consumed by the transaction, in the smallest unit of the chain&#39;s native token. For example, the value is in wei for Ethereum. | [optional] 
**evm_transaction_type** | **int** | The transaction envelope type defined by the chain. This property describes the on-chain transaction format, not the Cobo transaction type returned by [Get transaction information](https://www.cobo.com/developers/v2/api-references/transactions/get-transaction-information). - &#x60;0&#x60;: A legacy transaction. - &#x60;1&#x60;: An access list transaction, as defined in EIP-2930. - &#x60;2&#x60;: A dynamic fee transaction, as defined in EIP-1559.  | [optional] 
**logs_bloom** | **str** | The bloom filter of the event logs emitted during the execution of the transaction, which can be used to quickly check whether the transaction emitted a specific log. The value is a 256-byte hexadecimal string. | [optional] 
**logs** | [**List[TransactionReceiptLog]**](TransactionReceiptLog.md) | The event logs emitted during the execution of the transaction, in the order in which they were emitted. The array is empty if the transaction emitted no logs. A maximum of 1,000 logs are returned. If the transaction emitted more logs, only the first 1,000 are returned and &#x60;logs_truncated&#x60; is &#x60;true&#x60;. | 
**logs_truncated** | **bool** | Whether the event logs returned in &#x60;logs&#x60; were truncated. - &#x60;true&#x60;: The transaction emitted more than 1,000 logs and only the first 1,000 are returned. - &#x60;false&#x60;: All the logs emitted by the transaction are returned.  | 

## Example

```python
from cobo_waas2.models.transaction_receipt import TransactionReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReceipt from a JSON string
transaction_receipt_instance = TransactionReceipt.from_json(json)
# print the JSON string representation of the object
print(TransactionReceipt.to_json())

# convert the object into a dict
transaction_receipt_dict = transaction_receipt_instance.to_dict()
# create an instance of TransactionReceipt from a dict
transaction_receipt_from_dict = TransactionReceipt.from_dict(transaction_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


