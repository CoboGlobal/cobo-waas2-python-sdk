# ListExchanges200ResponseInner

The information about the supported exchange.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | 
**supported_trading_account_types** | **List[str]** | The supported trading account types of this exchange. | 

## Example

```python
from cobo_waas2.models.list_exchanges200_response_inner import ListExchanges200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListExchanges200ResponseInner from a JSON string
list_exchanges200_response_inner_instance = ListExchanges200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListExchanges200ResponseInner.to_json())

# convert the object into a dict
list_exchanges200_response_inner_dict = list_exchanges200_response_inner_instance.to_dict()
# create an instance of ListExchanges200ResponseInner from a dict
list_exchanges200_response_inner_from_dict = ListExchanges200ResponseInner.from_dict(list_exchanges200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


