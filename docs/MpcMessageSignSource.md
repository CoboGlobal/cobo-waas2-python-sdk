# MpcMessageSignSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**MessageSignSourceType**](MessageSignSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 

## Example

```python
from cobo_waas2.models.mpc_message_sign_source import MpcMessageSignSource

# TODO update the JSON string below
json = "{}"
# create an instance of MpcMessageSignSource from a JSON string
mpc_message_sign_source_instance = MpcMessageSignSource.from_json(json)
# print the JSON string representation of the object
print(MpcMessageSignSource.to_json())

# convert the object into a dict
mpc_message_sign_source_dict = mpc_message_sign_source_instance.to_dict()
# create an instance of MpcMessageSignSource from a dict
mpc_message_sign_source_from_dict = MpcMessageSignSource.from_dict(mpc_message_sign_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


