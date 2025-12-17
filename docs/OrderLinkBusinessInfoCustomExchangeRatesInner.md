# OrderLinkBusinessInfoCustomExchangeRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The cryptocurrency token ID | 
**exchange_rate** | **str** | The fixed exchange rate to use for this token | 

## Example

```python
from cobo_waas2.models.order_link_business_info_custom_exchange_rates_inner import OrderLinkBusinessInfoCustomExchangeRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLinkBusinessInfoCustomExchangeRatesInner from a JSON string
order_link_business_info_custom_exchange_rates_inner_instance = OrderLinkBusinessInfoCustomExchangeRatesInner.from_json(json)
# print the JSON string representation of the object
print(OrderLinkBusinessInfoCustomExchangeRatesInner.to_json())

# convert the object into a dict
order_link_business_info_custom_exchange_rates_inner_dict = order_link_business_info_custom_exchange_rates_inner_instance.to_dict()
# create an instance of OrderLinkBusinessInfoCustomExchangeRatesInner from a dict
order_link_business_info_custom_exchange_rates_inner_from_dict = OrderLinkBusinessInfoCustomExchangeRatesInner.from_dict(order_link_business_info_custom_exchange_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


