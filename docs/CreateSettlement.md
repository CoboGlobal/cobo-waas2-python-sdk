# CreateSettlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. Specify this field when &#x60;settlement_type&#x60; is set to &#x60;Merchant&#x60;. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency you want to settle. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | [optional] 
**currency** | **str** | The fiat currency for settling the cryptocurrency. Currently, only &#x60;USD&#x60; is supported. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;. | [optional] 
**amount** | **str** | The settlement amount. When settling merchant balance from orders (&#x60;acquiring_type&#x60; is &#x60;Order&#x60; and &#x60;settlement_type&#x60; is &#x60;Merchant&#x60;), do not specify this field as the settlement amount will be automatically calculated based on the order amounts. - If &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;, this represents the settlement amount in the specified cryptocurrency. - If &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;, this represents the settlement amount in the specified fiat currency.  | [optional] 
**bank_account_id** | **str** | The ID of the bank account where the settled funds will be deposited. This field is only applicable when &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;. Call [List all bank accounts](/v2/api-references/payment/list-all-bank-accounts) to retrieve the IDs of registered bank accounts.  | [optional] 
**crypto_address_id** | **str** | The ID of the crypto address used for crypto withdrawal. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;.  Call [List all crypto addresses](/v2/api-references/payments/list-all-crypto-addresses) to retrieve registered crypto addresses.  | [optional] 
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


