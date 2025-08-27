# ListTokenizationBlocklistAddresses200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenizationBlocklistAddressNote]**](TokenizationBlocklistAddressNote.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from cobo_waas2.models.list_tokenization_blocklist_addresses200_response import ListTokenizationBlocklistAddresses200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTokenizationBlocklistAddresses200Response from a JSON string
list_tokenization_blocklist_addresses200_response_instance = ListTokenizationBlocklistAddresses200Response.from_json(json)
# print the JSON string representation of the object
print(ListTokenizationBlocklistAddresses200Response.to_json())

# convert the object into a dict
list_tokenization_blocklist_addresses200_response_dict = list_tokenization_blocklist_addresses200_response_instance.to_dict()
# create an instance of ListTokenizationBlocklistAddresses200Response from a dict
list_tokenization_blocklist_addresses200_response_from_dict = ListTokenizationBlocklistAddresses200Response.from_dict(list_tokenization_blocklist_addresses200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


