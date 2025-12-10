# GetExchangeRate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. | 
**currency** | **str** | The fiat currency. | 
**rate** | **str** | The current exchange rate between the specified currency pair. Expressed as the amount of fiat currency per one unit of cryptocurrency. For example, if the cryptocurrency is USDT and the fiat currency is USD, a rate of \&quot;0.99\&quot; means 1 USDT &#x3D; 0.99 USD. | 

## Example

```python
from cobo_waas2.models.get_exchange_rate200_response import GetExchangeRate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetExchangeRate200Response from a JSON string
get_exchange_rate200_response_instance = GetExchangeRate200Response.from_json(json)
# print the JSON string representation of the object
print(GetExchangeRate200Response.to_json())

# convert the object into a dict
get_exchange_rate200_response_dict = get_exchange_rate200_response_instance.to_dict()
# create an instance of GetExchangeRate200Response from a dict
get_exchange_rate200_response_from_dict = GetExchangeRate200Response.from_dict(get_exchange_rate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


