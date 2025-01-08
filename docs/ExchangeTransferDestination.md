# ExchangeTransferDestination

The information about the transaction destination type `ExchangeWallet`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  An Exchange Wallet (Sub Account) can only receive asset transfers from another Exchange Wallet.  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransferDestinationType**](TransferDestinationType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**trading_account_type** | **str** | The trading account type. | 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.exchange_transfer_destination import ExchangeTransferDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTransferDestination from a JSON string
exchange_transfer_destination_instance = ExchangeTransferDestination.from_json(json)
# print the JSON string representation of the object
print(ExchangeTransferDestination.to_json())

# convert the object into a dict
exchange_transfer_destination_dict = exchange_transfer_destination_instance.to_dict()
# create an instance of ExchangeTransferDestination from a dict
exchange_transfer_destination_from_dict = ExchangeTransferDestination.from_dict(exchange_transfer_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


