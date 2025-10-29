# CreateSettlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. Specify this field when &#x60;settlement_type&#x60; is set to &#x60;Merchant&#x60;. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency you want to settle. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;. Supported values: - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**amount** | **str** | The amount of cryptocurrency to be settled. When settling merchant balance from orders (&#x60;acquiring_type&#x60; is &#x60;Order&#x60; and &#x60;settlement_type&#x60; is &#x60;Merchant&#x60;), do not specify this field as the amount will be automatically calculated based on the order amounts.  | [optional] 
**crypto_address_id** | **str** | The ID of the crypto address used for crypto payouts. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;.  Call [List crypto addresses](https://www.cobo.com/developers/v2/api-references/payment/list-crypto-addresses) to retrieve registered crypto addresses.  | [optional] 
**order_ids** | **List[str]** |  | [optional] 

## Example

```python
from cobo_waas2.models.create_settlement import CreateSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSettlement from a JSON string
create_settlement_instance = CreateSettlement.from_json(json)
# print the JSON string representation of the object
print(CreateSettlement.to_json())

# convert the object into a dict
create_settlement_dict = create_settlement_instance.to_dict()
# create an instance of CreateSettlement from a dict
create_settlement_from_dict = CreateSettlement.from_dict(create_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


