# TSSKeyGenEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**TSSEventDataType**](TSSEventDataType.md) |  | 
**request_id** | **str** | The request ID. | [optional] 
**request_type** | [**TSSRequestTypeEenum**](TSSRequestTypeEenum.md) |  | [optional] 
**request_status** | [**TSSStatus**](TSSStatus.md) |  | [optional] 
**extra_info** | **str** | The extra info. | [optional] 
**failed_reason** | **str** | The failed reason. | [optional] 
**request_detail** | [**TSSKeyGenRequest**](TSSKeyGenRequest.md) |  | [optional] 
**result** | [**TSSGroup**](TSSGroup.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_key_gen_event_data import TSSKeyGenEventData

# TODO update the JSON string below
json = "{}"
# create an instance of TSSKeyGenEventData from a JSON string
tss_key_gen_event_data_instance = TSSKeyGenEventData.from_json(json)
# print the JSON string representation of the object
print(TSSKeyGenEventData.to_json())

# convert the object into a dict
tss_key_gen_event_data_dict = tss_key_gen_event_data_instance.to_dict()
# create an instance of TSSKeyGenEventData from a dict
tss_key_gen_event_data_from_dict = TSSKeyGenEventData.from_dict(tss_key_gen_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


