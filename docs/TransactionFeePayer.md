# TransactionFeePayer

The extra information of fee payer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_type** | [**TransactionExtraType**](TransactionExtraType.md) |  | 
**fee_payer** | **str** | The address of the designated Solana fee payer account that covers the transaction fees, separating the fee payment from the main signer or source account. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_fee_payer import TransactionFeePayer

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFeePayer from a JSON string
transaction_fee_payer_instance = TransactionFeePayer.from_json(json)
# print the JSON string representation of the object
print(TransactionFeePayer.to_json())

# convert the object into a dict
transaction_fee_payer_dict = transaction_fee_payer_instance.to_dict()
# create an instance of TransactionFeePayer from a dict
transaction_fee_payer_from_dict = TransactionFeePayer.from_dict(transaction_fee_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


