# TransactionDepositToWalletDestination

Information about the transaction destination type `DepositToWallet`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**trading_account_type** | **str** | The trading account type. | [optional] 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | [optional] 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.transaction_deposit_to_wallet_destination import TransactionDepositToWalletDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDepositToWalletDestination from a JSON string
transaction_deposit_to_wallet_destination_instance = TransactionDepositToWalletDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionDepositToWalletDestination.to_json())

# convert the object into a dict
transaction_deposit_to_wallet_destination_dict = transaction_deposit_to_wallet_destination_instance.to_dict()
# create an instance of TransactionDepositToWalletDestination from a dict
transaction_deposit_to_wallet_destination_from_dict = TransactionDepositToWalletDestination.from_dict(transaction_deposit_to_wallet_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


