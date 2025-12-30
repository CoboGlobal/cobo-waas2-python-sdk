# OrderLinkBusinessInfoPayableAmountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency used for payment. Supported values: - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**amount** | **str** | The payable amount in the specified currency. | 

## Example

```python
from cobo_waas2.models.order_link_business_info_payable_amounts_inner import OrderLinkBusinessInfoPayableAmountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLinkBusinessInfoPayableAmountsInner from a JSON string
order_link_business_info_payable_amounts_inner_instance = OrderLinkBusinessInfoPayableAmountsInner.from_json(json)
# print the JSON string representation of the object
print(OrderLinkBusinessInfoPayableAmountsInner.to_json())

# convert the object into a dict
order_link_business_info_payable_amounts_inner_dict = order_link_business_info_payable_amounts_inner_instance.to_dict()
# create an instance of OrderLinkBusinessInfoPayableAmountsInner from a dict
order_link_business_info_payable_amounts_inner_from_dict = OrderLinkBusinessInfoPayableAmountsInner.from_dict(order_link_business_info_payable_amounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


