# CreateAddressBooksParam

The request body to batch create address book.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_books** | [**List[CreateAddressBookParam]**](CreateAddressBookParam.md) |  | 

## Example

```python
from cobo_waas2.models.create_address_books_param import CreateAddressBooksParam

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressBooksParam from a JSON string
create_address_books_param_instance = CreateAddressBooksParam.from_json(json)
# print the JSON string representation of the object
print(CreateAddressBooksParam.to_json())

# convert the object into a dict
create_address_books_param_dict = create_address_books_param_instance.to_dict()
# create an instance of CreateAddressBooksParam from a dict
create_address_books_param_from_dict = CreateAddressBooksParam.from_dict(create_address_books_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


