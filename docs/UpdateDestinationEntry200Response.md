# UpdateDestinationEntry200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account** | [**DestinationBankAccount**](DestinationBankAccount.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.update_destination_entry200_response import UpdateDestinationEntry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDestinationEntry200Response from a JSON string
update_destination_entry200_response_instance = UpdateDestinationEntry200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateDestinationEntry200Response.to_json())

# convert the object into a dict
update_destination_entry200_response_dict = update_destination_entry200_response_instance.to_dict()
# create an instance of UpdateDestinationEntry200Response from a dict
update_destination_entry200_response_from_dict = UpdateDestinationEntry200Response.from_dict(update_destination_entry200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


