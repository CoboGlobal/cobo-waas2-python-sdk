# TransactionUtxoFee

The transaction fee actually charged by the chain that uses the UTXO fee model, such as Bitcoin.  The transaction fee is calculated by multiplying the fee rate by the transaction size. This can be expressed as: Transaction fee = fee rate * transaction size.  Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_rate** | **str** | The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain. | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | [optional] 
**fee_used** | **str** | The actually charged transaction fee. | [optional] 
**estimated_fee_used** | **str** | The estimated transaction fee. | [optional] 
**max_fee_amount** | **str** | The maximum fee that you are willing to pay for the transaction. The transaction will fail if the transaction fee exceeds the maximum fee. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_utxo_fee import TransactionUtxoFee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUtxoFee from a JSON string
transaction_utxo_fee_instance = TransactionUtxoFee.from_json(json)
# print the JSON string representation of the object
print(TransactionUtxoFee.to_json())

# convert the object into a dict
transaction_utxo_fee_dict = transaction_utxo_fee_instance.to_dict()
# create an instance of TransactionUtxoFee from a dict
transaction_utxo_fee_from_dict = TransactionUtxoFee.from_dict(transaction_utxo_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


