# TSSRequest

The data for the TSS request information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tss_request_id** | **str** | The TSS request ID. | [optional] 
**source_key_share_holder_group** | [**SourceGroup**](SourceGroup.md) |  | [optional] 
**target_key_share_holder_group_id** | **str** | The target key share holder group ID. | [optional] 
**type** | [**TSSRequestType**](TSSRequestType.md) |  | [optional] 
**status** | [**TSSRequestStatus**](TSSRequestStatus.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tss_request import TSSRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TSSRequest from a JSON string
tss_request_instance = TSSRequest.from_json(json)
# print the JSON string representation of the object
print(TSSRequest.to_json())

# convert the object into a dict
tss_request_dict = tss_request_instance.to_dict()
# create an instance of TSSRequest from a dict
tss_request_from_dict = TSSRequest.from_dict(tss_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


