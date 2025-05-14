# PaymentTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | The transaction ID. | 
**tx_hash** | **str** | The transaction hash. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency. | [optional] 
**from_address** | **str** | The source address of the transaction. | 
**to_address** | **str** | The destination address of the transaction. | 
**amount** | **str** | The amount of cryptocurrency transferred, as a decimal string. | 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**created_timestamp** | **int** | The time when the transaction was created, in Unix timestamp format, measured in milliseconds. | 
**updated_timestamp** | **int** | The time when the transaction was updated, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.payment_transaction import PaymentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransaction from a JSON string
payment_transaction_instance = PaymentTransaction.from_json(json)
# print the JSON string representation of the object
print(PaymentTransaction.to_json())

# convert the object into a dict
payment_transaction_dict = payment_transaction_instance.to_dict()
# create an instance of PaymentTransaction from a dict
payment_transaction_from_dict = PaymentTransaction.from_dict(payment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


