# TransactionExchangeWalletSource

Information about the transaction source types `Main` and `Sub`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**trading_account_type** | **str** | The exchange trading account or a sub-wallet ID. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_exchange_wallet_source import TransactionExchangeWalletSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionExchangeWalletSource from a JSON string
transaction_exchange_wallet_source_instance = TransactionExchangeWalletSource.from_json(json)
# print the JSON string representation of the object
print(TransactionExchangeWalletSource.to_json())

# convert the object into a dict
transaction_exchange_wallet_source_dict = transaction_exchange_wallet_source_instance.to_dict()
# create an instance of TransactionExchangeWalletSource from a dict
transaction_exchange_wallet_source_from_dict = TransactionExchangeWalletSource.from_dict(transaction_exchange_wallet_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


