# CreateSettlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency you want to settle. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | [optional] 
**currency** | **str** | The fiat currency for settling the cryptocurrency. Currently, only &#x60;USD&#x60; is supported. | [optional] [default to 'USD']
**amount** | **str** | The settlement amount. - If &#x60;token_id&#x60; is specified, this represents the settlement amount in the specified cryptocurrency. - If &#x60;token_id&#x60; is not specified, this represents the settlement amount in the specified fiat currency. | [optional] 
**bank_account_id** | **str** | The ID of the bank account where the settled funds will be deposited. | [optional] 
**settlement_type** | [**SettlementType**](SettlementType.md) |  | [optional] 

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


