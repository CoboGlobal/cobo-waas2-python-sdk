# TokenizationAllowlistAddressesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenizationAllowlistAddressNote]**](TokenizationAllowlistAddressNote.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_allowlist_addresses_response import TokenizationAllowlistAddressesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationAllowlistAddressesResponse from a JSON string
tokenization_allowlist_addresses_response_instance = TokenizationAllowlistAddressesResponse.from_json(json)
# print the JSON string representation of the object
print(TokenizationAllowlistAddressesResponse.to_json())

# convert the object into a dict
tokenization_allowlist_addresses_response_dict = tokenization_allowlist_addresses_response_instance.to_dict()
# create an instance of TokenizationAllowlistAddressesResponse from a dict
tokenization_allowlist_addresses_response_from_dict = TokenizationAllowlistAddressesResponse.from_dict(tokenization_allowlist_addresses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


