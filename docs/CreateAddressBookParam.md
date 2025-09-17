# CreateAddressBookParam

The request body to add an address to your Address Book.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_ids** | **List[str]** | A list of chain IDs. | 
**address** | **str** | The wallet address. | 
**memo** | **str** | Optional memo or tag required by some chains. | [optional] 
**label** | **str** | A user-defined label for the address. | [optional] 
**email** | **str** | The email of the address owner. | [optional] 

## Example

```python
from cobo_waas2.models.create_address_book_param import CreateAddressBookParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressBookParam from a JSON string
create_address_book_param_instance = CreateAddressBookParam.from_json(json)
# print the JSON string representation of the object
print(CreateAddressBookParam.to_json())

# convert the object into a dict
create_address_book_param_dict = create_address_book_param_instance.to_dict()
# create an instance of CreateAddressBookParam from a dict
create_address_book_param_from_dict = CreateAddressBookParam.from_dict(create_address_book_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


