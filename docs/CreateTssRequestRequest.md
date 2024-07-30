# CreateTssRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TSSRequestType**](TSSRequestType.md) |  | 
**target_key_share_holder_group_id** | **str** | The target key share holder group ID. | 
**source_key_share_holder_group** | [**SourceGroup**](SourceGroup.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_tss_request_request import CreateTssRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTssRequestRequest from a JSON string
create_tss_request_request_instance = CreateTssRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTssRequestRequest.to_json())

# convert the object into a dict
create_tss_request_request_dict = create_tss_request_request_instance.to_dict()
# create an instance of CreateTssRequestRequest from a dict
create_tss_request_request_from_dict = CreateTssRequestRequest.from_dict(create_tss_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


