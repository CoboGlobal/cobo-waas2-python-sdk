# PaymentPayoutTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The WaaS transaction ID. | 
**amount** | [**PaymentAssetAmount**](PaymentAssetAmount.md) | The transaction amount. | 
**tx_hash** | **str** | The blockchain transaction hash. | 
**result** | [**PaymentPayoutTransactionResult**](PaymentPayoutTransactionResult.md) |  | 
**failed_reason** | [**PaymentFailedReason**](PaymentFailedReason.md) |  | 

## Example

```python
from cobo_waas2.models.payment_payout_transaction import PaymentPayoutTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPayoutTransaction from a JSON string
payment_payout_transaction_instance = PaymentPayoutTransaction.from_json(json)
# print the JSON string representation of the object
print(PaymentPayoutTransaction.to_json())

# convert the object into a dict
payment_payout_transaction_dict = payment_payout_transaction_instance.to_dict()
# create an instance of PaymentPayoutTransaction from a dict
payment_payout_transaction_from_dict = PaymentPayoutTransaction.from_dict(payment_payout_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


