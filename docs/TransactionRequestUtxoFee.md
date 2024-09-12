# TransactionRequestUtxoFee

The preset properties to limit transaction fee.  In the UTXO fee model, the transaction fee is calculated by multiplying the fee rate by the transaction size. This can be expressed as: Transaction fee = fee rate * transaction size.   You can specify the maximum fee amount to limit the transaction fee. The transaction will fail if the transaction fee exceeds the specified maximum fee amount.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token ID of the transaction fee. | 
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 

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


