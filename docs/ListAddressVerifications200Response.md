# ListAddressVerifications200Response

Paginated list of address verification records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AddressVerification]**](AddressVerification.md) | The page of address verification records. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.list_address_verifications200_response import ListAddressVerifications200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAddressVerifications200Response from a JSON string
list_address_verifications200_response_instance = ListAddressVerifications200Response.from_json(json)
# print the JSON string representation of the object
print(ListAddressVerifications200Response.to_json())

# convert the object into a dict
list_address_verifications200_response_dict = list_address_verifications200_response_instance.to_dict()
# create an instance of ListAddressVerifications200Response from a dict
list_address_verifications200_response_from_dict = ListAddressVerifications200Response.from_dict(list_address_verifications200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


