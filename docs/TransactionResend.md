# TransactionResend

The information about the request to resend transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | 

## Example

```python
from cobo_waas2.models.transaction_resend import TransactionResend

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResend from a JSON string
transaction_resend_instance = TransactionResend.from_json(json)
# print the JSON string representation of the object
print(TransactionResend.to_json())

# convert the object into a dict
transaction_resend_dict = transaction_resend_instance.to_dict()
# create an instance of TransactionResend from a dict
transaction_resend_from_dict = TransactionResend.from_dict(transaction_resend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


