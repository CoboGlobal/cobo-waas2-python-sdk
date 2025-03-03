# MessageSignSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**MessageSignSourceType**](MessageSignSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 
**mpc_used_key_share_holder_group** | [**MpcSigningGroup**](MpcSigningGroup.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.message_sign_source import MessageSignSource

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSignSource from a JSON string
message_sign_source_instance = MessageSignSource.from_json(json)
# print the JSON string representation of the object
print(MessageSignSource.to_json())

# convert the object into a dict
message_sign_source_dict = message_sign_source_instance.to_dict()
# create an instance of MessageSignSource from a dict
message_sign_source_from_dict = MessageSignSource.from_dict(message_sign_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


