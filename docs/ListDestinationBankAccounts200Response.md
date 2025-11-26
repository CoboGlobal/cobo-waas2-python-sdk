# ListDestinationBankAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DestinationBankAccountDetail]**](DestinationBankAccountDetail.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_destination_bank_accounts200_response import ListDestinationBankAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDestinationBankAccounts200Response from a JSON string
list_destination_bank_accounts200_response_instance = ListDestinationBankAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(ListDestinationBankAccounts200Response.to_json())

# convert the object into a dict
list_destination_bank_accounts200_response_dict = list_destination_bank_accounts200_response_instance.to_dict()
# create an instance of ListDestinationBankAccounts200Response from a dict
list_destination_bank_accounts200_response_from_dict = ListDestinationBankAccounts200Response.from_dict(list_destination_bank_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


