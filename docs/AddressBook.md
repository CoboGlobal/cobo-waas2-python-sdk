# AddressBook

The information of an address book entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | The organization ID. | 
**entry_id** | **str** | The entry ID. | 
**address** | **str** | The wallet address. | 
**memo** | **str** | The memo. | [optional] 
**wallet_name** | **str** | The wallet name. | [optional] 
**wallet_type** | [**WalletType**](WalletType.md) |  | [optional] 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | [optional] 
**label** | **str** | The address label. | 
**chain_ids** | **List[str]** | A list of chain IDs. | [optional] 
**email** | **str** | The email of the address owner. | [optional] 
**encoding** | [**AddressEncoding**](AddressEncoding.md) |  | [optional] 

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


