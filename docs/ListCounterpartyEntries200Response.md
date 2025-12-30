# ListCounterpartyEntries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_addresses** | [**List[CounterpartyWalletAddressDetail]**](CounterpartyWalletAddressDetail.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_counterparty_entries200_response import ListCounterpartyEntries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCounterpartyEntries200Response from a JSON string
list_counterparty_entries200_response_instance = ListCounterpartyEntries200Response.from_json(json)
# print the JSON string representation of the object
print(ListCounterpartyEntries200Response.to_json())

# convert the object into a dict
list_counterparty_entries200_response_dict = list_counterparty_entries200_response_instance.to_dict()
# create an instance of ListCounterpartyEntries200Response from a dict
list_counterparty_entries200_response_from_dict = ListCounterpartyEntries200Response.from_dict(list_counterparty_entries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


