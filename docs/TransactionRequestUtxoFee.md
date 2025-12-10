# TransactionRequestUtxoFee

The preset properties to limit transaction fee.  In the UTXO fee model, the transaction fee is calculated by multiplying the fee rate by the transaction size. This can be expressed as: Transaction fee = fee rate * transaction size. For more information about the UTXO fee model, see [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  You can specify the maximum fee amount to limit the transaction fee. The transaction will fail if the transaction fee exceeds the specified maximum fee amount.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | [optional] 
**fallback** | **bool** | Indicates whether the estimated fee is generated from Cobo’s fallback mechanism. When the estimated transaction belongs to a UTXO-based chain and the specified address does not have sufficient balance to cover the on-chain fee, this field will be set to &#x60;true&#x60;. In this case, the returned fee value is estimated by Cobo’s internal fallback strategy, which is typically higher than the actual on-chain fee. When &#x60;fallback&#x60; is &#x60;true&#x60;, please use the estimated fee value with caution. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. Provide the value without applying precision. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_request_utxo_fee import TransactionRequestUtxoFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestUtxoFee from a JSON string
transaction_request_utxo_fee_instance = TransactionRequestUtxoFee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestUtxoFee.to_json())

# convert the object into a dict
transaction_request_utxo_fee_dict = transaction_request_utxo_fee_instance.to_dict()
# create an instance of TransactionRequestUtxoFee from a dict
transaction_request_utxo_fee_from_dict = TransactionRequestUtxoFee.from_dict(transaction_request_utxo_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


