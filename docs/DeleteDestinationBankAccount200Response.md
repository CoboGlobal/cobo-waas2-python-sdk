# DeleteDestinationBankAccount200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_id** | **str** | The destination bank account ID. | 

## Example

```python
from cobo_waas2.models.delete_destination_bank_account200_response import DeleteDestinationBankAccount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDestinationBankAccount200Response from a JSON string
delete_destination_bank_account200_response_instance = DeleteDestinationBankAccount200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteDestinationBankAccount200Response.to_json())

# convert the object into a dict
delete_destination_bank_account200_response_dict = delete_destination_bank_account200_response_instance.to_dict()
# create an instance of DeleteDestinationBankAccount200Response from a dict
delete_destination_bank_account200_response_from_dict = DeleteDestinationBankAccount200Response.from_dict(delete_destination_bank_account200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


