# ListFiatEntryKyc200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FiatEntryKyc]**](FiatEntryKyc.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_fiat_entry_kyc200_response import ListFiatEntryKyc200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListFiatEntryKyc200Response from a JSON string
list_fiat_entry_kyc200_response_instance = ListFiatEntryKyc200Response.from_json(json)
# print the JSON string representation of the object
print(ListFiatEntryKyc200Response.to_json())

# convert the object into a dict
list_fiat_entry_kyc200_response_dict = list_fiat_entry_kyc200_response_instance.to_dict()
# create an instance of ListFiatEntryKyc200Response from a dict
list_fiat_entry_kyc200_response_from_dict = ListFiatEntryKyc200Response.from_dict(list_fiat_entry_kyc200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


