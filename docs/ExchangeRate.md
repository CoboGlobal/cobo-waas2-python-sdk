# ExchangeRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which identifies the cryptocurrency. | 
**currency** | **str** | The fiat currency. | 
**rate** | **str** | The current exchange rate between the specified currency pair. Expressed as the amount of fiat currency per one unit of cryptocurrency. For example, if the cryptocurrency is USDT and the fiat currency is USD, a rate of \&quot;0.99\&quot; means 1 USDT &#x3D; 0.99 USD. | 

## Example

```python
from cobo_waas2.models.exchange_rate import ExchangeRate

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRate from a JSON string
exchange_rate_instance = ExchangeRate.from_json(json)
# print the JSON string representation of the object
print(ExchangeRate.to_json())

# convert the object into a dict
exchange_rate_dict = exchange_rate_instance.to_dict()
# create an instance of ExchangeRate from a dict
exchange_rate_from_dict = ExchangeRate.from_dict(exchange_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


