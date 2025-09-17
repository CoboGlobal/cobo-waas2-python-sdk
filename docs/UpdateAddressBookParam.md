# UpdateAddressBookParam

The request body to update Address Book.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_ids** | **List[str]** | A list of chain IDs. | 
**memo** | **str** | Optional memo or tag required by some chains. | [optional] 
**label** | **str** | A user-defined label for the address. | [optional] 
**email** | **str** | Email of the address owner. | [optional] 

## Example

```python
from cobo_waas2.models.update_address_book_param import UpdateAddressBookParam

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAddressBookParam from a JSON string
update_address_book_param_instance = UpdateAddressBookParam.from_json(json)
# print the JSON string representation of the object
print(UpdateAddressBookParam.to_json())

# convert the object into a dict
update_address_book_param_dict = update_address_book_param_instance.to_dict()
# create an instance of UpdateAddressBookParam from a dict
update_address_book_param_from_dict = UpdateAddressBookParam.from_dict(update_address_book_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


