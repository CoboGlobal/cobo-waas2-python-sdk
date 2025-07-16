# TransactionRequestFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. Provide the value without applying precision. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 
**gas_limit** | **str** | The maximum amount of gas your transaction is allowed to consume. | [optional] 
**max_fee_per_gas** | **str** | The maximum gas fee per gas unit used on the chain, in wei. | 
**max_priority_fee_per_gas** | **str** | The maximum priority fee per gas unit used, in wei. The maximum priority fee represents the highest amount of miner tips that you are willing to pay for your transaction. | 
**gas_price** | **str** | The gas price, in wei. The gas price represents the amount of ETH that must be paid to validators for processing transactions per gas unit used. | 
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | [optional] 
**compute_unit_price** | **str** | The price paid per compute unit. This value determines the priority fee for the transaction, allowing you to increase inclusion probability in congested conditions. | 
**compute_unit_limit** | **str** | The maximum number of compute units your transaction is allowed to consume. It sets an upper bound on computational resource usage to prevent overload. | 
**gas_premium** | **str** | An optional tip you can include to prioritize your transaction. The gas premium incentivizes miners to include your transaction sooner than those offering only the base fee. | 
**gas_fee_cap** | **str** | The maximum gas price you are willing to pay per unit of gas. | 

## Example

```python
from cobo_waas2.models.transaction_request_fee import TransactionRequestFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestFee from a JSON string
transaction_request_fee_instance = TransactionRequestFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestFee.to_json())

# convert the object into a dict
transaction_request_fee_dict = transaction_request_fee_instance.to_dict()
# create an instance of TransactionRequestFee from a dict
transaction_request_fee_from_dict = TransactionRequestFee.from_dict(transaction_request_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


