# TransactionDepositFromWalletSource

Information about the transaction source type `DepositFromWallet`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | 
**trading_account_type** | **str** | The exchange trading account or a sub-wallet ID. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_deposit_from_wallet_source import TransactionDepositFromWalletSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDepositFromWalletSource from a JSON string
transaction_deposit_from_wallet_source_instance = TransactionDepositFromWalletSource.from_json(json)
# print the JSON string representation of the object
print(TransactionDepositFromWalletSource.to_json())

# convert the object into a dict
transaction_deposit_from_wallet_source_dict = transaction_deposit_from_wallet_source_instance.to_dict()
# create an instance of TransactionDepositFromWalletSource from a dict
transaction_deposit_from_wallet_source_from_dict = TransactionDepositFromWalletSource.from_dict(transaction_deposit_from_wallet_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


