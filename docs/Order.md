# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order ID. | 
**merchant_id** | **str** | The merchant ID. | [optional] 
**token_id** | **str** |  The ID of the cryptocurrency used for payment. Supported tokens:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**chain_id** | **str** |  The ID of the blockchain network where the payment transaction should be made. Supported chains:  - USDC: &#x60;ETH&#x60;, &#x60;ARBITRUM&#x60;, &#x60;SOL&#x60;, &#x60;BASE&#x60;, &#x60;MATIC&#x60;, &#x60;BSC&#x60; - USDT: &#x60;TRON&#x60;, &#x60;ETH&#x60;, &#x60;ARBITRUM&#x60;, &#x60;SOL&#x60;, &#x60;BASE&#x60;, &#x60;MATIC&#x60;, &#x60;BSC&#x60;  | 
**payable_amount** | **str** | The cryptocurrency amount to be paid for this order. | 
**receive_address** | **str** | The recipient wallet address to be used for the payment transaction. | 
**currency** | **str** | The fiat currency of the order. | 
**order_amount** | **str** | The base amount of the order in fiat currency, excluding the developer fee (specified in &#x60;fee_amount&#x60;). | 
**fee_amount** | **str** | The developer fee for the order in fiat currency. It is added to the base amount (&#x60;order_amount&#x60;) to determine the final charge. | 
**exchange_rate** | **str** | The exchange rate between a currency pair. Expressed as the amount of fiat currency per one unit of cryptocurrency. For example, if the cryptocurrency is USDT and the fiat currency is USD, a rate of \&quot;0.99\&quot; means 1 USDT &#x3D; 0.99 USD. | 
**expired_at** | **int** | The expiration time of the pay-in order, represented as a UNIX timestamp in seconds. | [optional] 
**merchant_order_code** | **str** | A unique reference code assigned by the merchant to identify this order in their system. | [optional] 
**psp_order_code** | **str** | A unique reference code assigned by the developer to identify this order in their system. | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**received_token_amount** | **str** | The total cryptocurrency amount received for this order. Updates until the expiration time. Precision matches the token standard (e.g., 6 decimals for USDT). | 
**created_timestamp** | **int** | The creation time of the order, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the order, represented as a UNIX timestamp in seconds. | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of transactions associated with this pay-in order. Each transaction represents a separate blockchain operation related to the pay-in process. | [optional] 
**settlement_status** | [**SettleStatus**](SettleStatus.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


