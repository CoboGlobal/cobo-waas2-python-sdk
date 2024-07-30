# TransactionExchangeWalletSource

Information about the transaction source, which varies depending on whether you are the initiator or the receiver of the transaction.   - As the initiator, you will see detailed information about the transaction source, and the `source` will be displayed as one of the following wallet sub-types: `Asset`, `Org-Controlled`, `User-Controlled`, `Safe{Wallet}`, `Main`, or `Sub`. - As the receiver, you will see the `source` as either `DepositFromAddress`, `DepositFromWallet`, or `DepositFromLoop`. If the transaction is from the Loop transfer network, the source will be `DepositFromLoop`. Otherwise, it will be either `DepositFromWallet` (indicating an Exchange Wallet) or `DepositFromAddress` (indicating other wallet type than an Exchange Wallet or an external address). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**sub_wallet_id** | **str** | The exchange trading account or a sub-wallet ID. | [optional] 

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


