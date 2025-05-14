# TSSKeySignEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**TSSEventDataType**](TSSEventDataType.md) |  | 
**request_id** | **str** | The request ID. | [optional] 
**request_type** | [**TSSRequestTypeEenum**](TSSRequestTypeEenum.md) |  | [optional] 
**request_status** | [**TSSStatus**](TSSStatus.md) |  | [optional] 
**extra_info** | **str** | The extra info. | [optional] 
**failed_reason** | **str** | The failed reason. | [optional] 
**request_detail** | [**TSSKeySignRequest**](TSSKeySignRequest.md) |  | [optional] 
**result** | [**TSSSignatures**](TSSSignatures.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_sign_event_data import TSSKeySignEventData

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeySignEventData from a JSON string
tss_key_sign_event_data_instance = TSSKeySignEventData.from_json(json)
# print the JSON string representation of the object
print(TSSKeySignEventData.to_json())

# convert the object into a dict
tss_key_sign_event_data_dict = tss_key_sign_event_data_instance.to_dict()
# create an instance of TSSKeySignEventData from a dict
tss_key_sign_event_data_from_dict = TSSKeySignEventData.from_dict(tss_key_sign_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


