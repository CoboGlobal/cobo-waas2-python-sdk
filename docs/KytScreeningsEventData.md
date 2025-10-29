# KytScreeningsEventData

The KYT screening information about a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | 
**transaction_type** | [**KytScreeningsTransactionType**](KytScreeningsTransactionType.md) |  | 
**review_status** | [**ReviewStatusType**](ReviewStatusType.md) |  | 
**funds_status** | [**FundsStatusType**](FundsStatusType.md) |  | 
**updated_timestamp** | **int** | The time when the KYT screening information was updated, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.kyt_screenings_event_data import KytScreeningsEventData

# TODO update the JSON string below
json = "{}"
# create an instance of KytScreeningsEventData from a JSON string
kyt_screenings_event_data_instance = KytScreeningsEventData.from_json(json)
# print the JSON string representation of the object
print(KytScreeningsEventData.to_json())

# convert the object into a dict
kyt_screenings_event_data_dict = kyt_screenings_event_data_instance.to_dict()
# create an instance of KytScreeningsEventData from a dict
kyt_screenings_event_data_from_dict = KytScreeningsEventData.from_dict(kyt_screenings_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


