# CreateTopUpAddresses201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TopUpAddress]**](TopUpAddress.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_top_up_addresses201_response import CreateTopUpAddresses201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopUpAddresses201Response from a JSON string
create_top_up_addresses201_response_instance = CreateTopUpAddresses201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTopUpAddresses201Response.to_json())

# convert the object into a dict
create_top_up_addresses201_response_dict = create_top_up_addresses201_response_instance.to_dict()
# create an instance of CreateTopUpAddresses201Response from a dict
create_top_up_addresses201_response_from_dict = CreateTopUpAddresses201Response.from_dict(create_top_up_addresses201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


