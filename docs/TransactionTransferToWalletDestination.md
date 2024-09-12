# TransactionTransferToWalletDestination

Information about the transaction destination type `ExchangeWallet`. Refer to [Transaction sources and destinations](/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**trading_account_type** | **str** | The trading account type. | [optional] 
**exchange_id** | [**ExchangeId**](ExchangeId.md) |  | [optional] 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.transaction_transfer_to_wallet_destination import TransactionTransferToWalletDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTransferToWalletDestination from a JSON string
transaction_transfer_to_wallet_destination_instance = TransactionTransferToWalletDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionTransferToWalletDestination.to_json())

# convert the object into a dict
transaction_transfer_to_wallet_destination_dict = transaction_transfer_to_wallet_destination_instance.to_dict()
# create an instance of TransactionTransferToWalletDestination from a dict
transaction_transfer_to_wallet_destination_from_dict = TransactionTransferToWalletDestination.from_dict(transaction_transfer_to_wallet_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


