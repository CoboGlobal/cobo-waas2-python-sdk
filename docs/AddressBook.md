# AddressBook

The data for address book entry information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**entry_id** | **str** |  | 
**address** | **str** | address. | 
**memo** | **str** | memo. | [optional] 
**wallet_name** | **str** | wallet name. | [optional] 
**wallet_type** | [**WalletType**](WalletType.md) |  | [optional] 
**label** | **str** | The label to address. | 
**email** | **str** | email. | [optional] 

## Example

```python
from cobo_waas2.models.address_book import AddressBook

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBook from a JSON string
address_book_instance = AddressBook.from_json(json)
# print the JSON string representation of the object
print(AddressBook.to_json())

# convert the object into a dict
address_book_dict = address_book_instance.to_dict()
# create an instance of AddressBook from a dict
address_book_from_dict = AddressBook.from_dict(address_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


