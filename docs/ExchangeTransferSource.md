# ExchangeTransferSource

The information about the transaction source types `Main` and `Sub`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Assets in an Exchange Wallet (Sub Account) can only be transferred to another Exchange Wallet.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**trading_account_type** | **str** | The trading account type. | 

## Example

```python
from cobo_waas2.models.exchange_transfer_source import ExchangeTransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTransferSource from a JSON string
exchange_transfer_source_instance = ExchangeTransferSource.from_json(json)
# print the JSON string representation of the object
print(ExchangeTransferSource.to_json())

# convert the object into a dict
exchange_transfer_source_dict = exchange_transfer_source_instance.to_dict()
# create an instance of ExchangeTransferSource from a dict
exchange_transfer_source_from_dict = ExchangeTransferSource.from_dict(exchange_transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


