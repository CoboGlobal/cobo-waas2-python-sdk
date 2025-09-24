# DispositionEventData

The disposition information about a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | 
**disposition_type** | [**DispositionType**](DispositionType.md) |  | 
**disposition_status** | [**DispositionStatus**](DispositionStatus.md) |  | 
**destination_address** | **str** | The blockchain address where the refund/isolated funds will be sent. | [optional] 
**disposition_amount** | **str** | The amount to be refund/isolated from the original transaction, specified as a numeric string. This value cannot exceed the total amount of the original transaction.  | [optional] 
**updated_timestamp** | **int** | The time when the disposition was updated, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.disposition_event_data import DispositionEventData

# TODO update the JSON string below
json = "{}"
# create an instance of DispositionEventData from a JSON string
disposition_event_data_instance = DispositionEventData.from_json(json)
# print the JSON string representation of the object
print(DispositionEventData.to_json())

# convert the object into a dict
disposition_event_data_dict = disposition_event_data_instance.to_dict()
# create an instance of DispositionEventData from a dict
disposition_event_data_from_dict = DispositionEventData.from_dict(disposition_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


