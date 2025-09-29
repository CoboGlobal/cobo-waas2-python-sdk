# KytScreeningsTransaction

The KYT screening status response containing transaction review and funds information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction that was screened. | 
**transaction_type** | [**KytScreeningsTransactionType**](KytScreeningsTransactionType.md) |  | 
**review_status** | [**ReviewStatusType**](ReviewStatusType.md) |  | 
**funds_status** | [**FundsStatusType**](FundsStatusType.md) |  | 

## Example

```python
from cobo_waas2.models.kyt_screenings_transaction import KytScreeningsTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of KytScreeningsTransaction from a JSON string
kyt_screenings_transaction_instance = KytScreeningsTransaction.from_json(json)
# print the JSON string representation of the object
print(KytScreeningsTransaction.to_json())

# convert the object into a dict
kyt_screenings_transaction_dict = kyt_screenings_transaction_instance.to_dict()
# create an instance of KytScreeningsTransaction from a dict
kyt_screenings_transaction_from_dict = KytScreeningsTransaction.from_dict(kyt_screenings_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


