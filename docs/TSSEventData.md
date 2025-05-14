# TSSEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**TSSEventDataType**](TSSEventDataType.md) |  | 
**request_id** | **str** | The request ID. | [optional] 
**request_type** | [**TSSRequestTypeEenum**](TSSRequestTypeEenum.md) |  | [optional] 
**request_status** | [**TSSStatus**](TSSStatus.md) |  | [optional] 
**extra_info** | **str** | The extra info. | [optional] 
**failed_reason** | **str** | The failed reason. | [optional] 
**request_detail** | [**TSSKeyShareSignRequest**](TSSKeyShareSignRequest.md) |  | [optional] 
**result** | [**TSSKeyShareSignSignatures**](TSSKeyShareSignSignatures.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_event_data import TSSEventData

# TODO update the JSON string below
json = "{}"
# create an instance of TSSEventData from a JSON string
tss_event_data_instance = TSSEventData.from_json(json)
# print the JSON string representation of the object
print(TSSEventData.to_json())

# convert the object into a dict
tss_event_data_dict = tss_event_data_instance.to_dict()
# create an instance of TSSEventData from a dict
tss_event_data_from_dict = TSSEventData.from_dict(tss_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


