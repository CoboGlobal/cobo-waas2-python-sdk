# KyaScreeningsEventData

Event data for KYA address screening status updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_id** | **str** | The unique system-generated identifier for this screening request (UUID format, fixed 36 characters). | 
**address** | **str** | The screened blockchain address. | 
**chain_id** | **str** | The chain identifier. | 
**status** | [**KyaScreeningStatus**](KyaScreeningStatus.md) |  | 
**created_timestamp** | **int** | The time when the screening request was created, in Unix timestamp format, measured in milliseconds. | 
**updated_timestamp** | **int** | The time when the screening status was updated, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.kya_screenings_event_data import KyaScreeningsEventData

# TODO update the JSON string below
json = "{}"
# create an instance of KyaScreeningsEventData from a JSON string
kya_screenings_event_data_instance = KyaScreeningsEventData.from_json(json)
# print the JSON string representation of the object
print(KyaScreeningsEventData.to_json())

# convert the object into a dict
kya_screenings_event_data_dict = kya_screenings_event_data_instance.to_dict()
# create an instance of KyaScreeningsEventData from a dict
kya_screenings_event_data_from_dict = KyaScreeningsEventData.from_dict(kya_screenings_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


