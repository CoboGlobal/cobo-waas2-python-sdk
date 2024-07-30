# CreateKeyShareHolder

When creating MainKeyGroup and SigningKeyGroup, the Cobo key share holder will be added automatically.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Key share holder&#39;s name. | [optional] 
**type** | [**KeyShareHolderType**](KeyShareHolderType.md) |  | [optional] 
**tss_node_id** | **str** | The TSS Node ID. | [optional] 

## Example

```python
from cobo_waas2.models.create_key_share_holder import CreateKeyShareHolder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyShareHolder from a JSON string
create_key_share_holder_instance = CreateKeyShareHolder.from_json(json)
# print the JSON string representation of the object
print(CreateKeyShareHolder.to_json())

# convert the object into a dict
create_key_share_holder_dict = create_key_share_holder_instance.to_dict()
# create an instance of CreateKeyShareHolder from a dict
create_key_share_holder_from_dict = CreateKeyShareHolder.from_dict(create_key_share_holder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


