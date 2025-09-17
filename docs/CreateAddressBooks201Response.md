# CreateAddressBooks201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AddressBook]**](AddressBook.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_address_books201_response import CreateAddressBooks201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressBooks201Response from a JSON string
create_address_books201_response_instance = CreateAddressBooks201Response.from_json(json)
# print the JSON string representation of the object
print(CreateAddressBooks201Response.to_json())

# convert the object into a dict
create_address_books201_response_dict = create_address_books201_response_instance.to_dict()
# create an instance of CreateAddressBooks201Response from a dict
create_address_books201_response_from_dict = CreateAddressBooks201Response.from_dict(create_address_books201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


