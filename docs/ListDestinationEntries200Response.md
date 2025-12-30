# ListDestinationEntries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_addresses** | [**List[DestinationWalletAddressDetail]**](DestinationWalletAddressDetail.md) |  | [optional] 
**bank_accounts** | [**List[DestinationBankAccountDetail]**](DestinationBankAccountDetail.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_destination_entries200_response import ListDestinationEntries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDestinationEntries200Response from a JSON string
list_destination_entries200_response_instance = ListDestinationEntries200Response.from_json(json)
# print the JSON string representation of the object
print(ListDestinationEntries200Response.to_json())

# convert the object into a dict
list_destination_entries200_response_dict = list_destination_entries200_response_instance.to_dict()
# create an instance of ListDestinationEntries200Response from a dict
list_destination_entries200_response_from_dict = ListDestinationEntries200Response.from_dict(list_destination_entries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


