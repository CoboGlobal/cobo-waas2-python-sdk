# QueryDestinationWhitelistEnabled200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_destination_whitelist** | **bool** | Indicates whether the destination whitelist is enabled. | 

## Example

```python
from cobo_waas2.models.query_destination_whitelist_enabled200_response import QueryDestinationWhitelistEnabled200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDestinationWhitelistEnabled200Response from a JSON string
query_destination_whitelist_enabled200_response_instance = QueryDestinationWhitelistEnabled200Response.from_json(json)
# print the JSON string representation of the object
print(QueryDestinationWhitelistEnabled200Response.to_json())

# convert the object into a dict
query_destination_whitelist_enabled200_response_dict = query_destination_whitelist_enabled200_response_instance.to_dict()
# create an instance of QueryDestinationWhitelistEnabled200Response from a dict
query_destination_whitelist_enabled200_response_from_dict = QueryDestinationWhitelistEnabled200Response.from_dict(query_destination_whitelist_enabled200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


