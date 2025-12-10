# EnableDestinationWhitelistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_destination_whitelist** | **bool** | Indicates whether to enable the destination whitelist. | 

## Example

```python
from cobo_waas2.models.enable_destination_whitelist_request import EnableDestinationWhitelistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableDestinationWhitelistRequest from a JSON string
enable_destination_whitelist_request_instance = EnableDestinationWhitelistRequest.from_json(json)
# print the JSON string representation of the object
print(EnableDestinationWhitelistRequest.to_json())

# convert the object into a dict
enable_destination_whitelist_request_dict = enable_destination_whitelist_request_instance.to_dict()
# create an instance of EnableDestinationWhitelistRequest from a dict
enable_destination_whitelist_request_from_dict = EnableDestinationWhitelistRequest.from_dict(enable_destination_whitelist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


