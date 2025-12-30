# UpdateDestinationEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_type** | [**EntryType**](EntryType.md) |  | [optional] 
**destination_id** | **str** | The destination ID. | 
**bank_account** | [**UpdateDestinationBankAccount**](UpdateDestinationBankAccount.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.update_destination_entry_request import UpdateDestinationEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDestinationEntryRequest from a JSON string
update_destination_entry_request_instance = UpdateDestinationEntryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDestinationEntryRequest.to_json())

# convert the object into a dict
update_destination_entry_request_dict = update_destination_entry_request_instance.to_dict()
# create an instance of UpdateDestinationEntryRequest from a dict
update_destination_entry_request_from_dict = UpdateDestinationEntryRequest.from_dict(update_destination_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


