# DeleteGuardPubkey201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_id** | **str** | The deleted Cobo Guard binding statement ID. | 

## Example

```python
from cobo_waas2.models.delete_guard_pubkey201_response import DeleteGuardPubkey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGuardPubkey201Response from a JSON string
delete_guard_pubkey201_response_instance = DeleteGuardPubkey201Response.from_json(json)
# print the JSON string representation of the object
print(DeleteGuardPubkey201Response.to_json())

# convert the object into a dict
delete_guard_pubkey201_response_dict = delete_guard_pubkey201_response_instance.to_dict()
# create an instance of DeleteGuardPubkey201Response from a dict
delete_guard_pubkey201_response_from_dict = DeleteGuardPubkey201Response.from_dict(delete_guard_pubkey201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


