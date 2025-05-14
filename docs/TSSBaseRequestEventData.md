# TSSBaseRequestEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**TSSEventDataType**](TSSEventDataType.md) |  | 
**request_id** | **str** | The request ID. | [optional] 
**request_type** | [**TSSRequestTypeEenum**](TSSRequestTypeEenum.md) |  | [optional] 
**request_status** | [**TSSStatus**](TSSStatus.md) |  | [optional] 
**extra_info** | **str** | The extra info. | [optional] 
**failed_reason** | **str** | The failed reason. | [optional] 

## Example

```python
from cobo_waas2.models.tss_base_request_event_data import TSSBaseRequestEventData

# TODO update the JSON string below
json = "{}"
# create an instance of TSSBaseRequestEventData from a JSON string
tss_base_request_event_data_instance = TSSBaseRequestEventData.from_json(json)
# print the JSON string representation of the object
print(TSSBaseRequestEventData.to_json())

# convert the object into a dict
tss_base_request_event_data_dict = tss_base_request_event_data_instance.to_dict()
# create an instance of TSSBaseRequestEventData from a dict
tss_base_request_event_data_from_dict = TSSBaseRequestEventData.from_dict(tss_base_request_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


