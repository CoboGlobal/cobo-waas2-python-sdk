# TransactionFeeStationWalletSource

The information about the transaction source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**wallet_id** | **str** | The Wallet ID. | 

## Example

```python
from cobo_waas2.models.transaction_fee_station_wallet_source import TransactionFeeStationWalletSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFeeStationWalletSource from a JSON string
transaction_fee_station_wallet_source_instance = TransactionFeeStationWalletSource.from_json(json)
# print the JSON string representation of the object
print(TransactionFeeStationWalletSource.to_json())

# convert the object into a dict
transaction_fee_station_wallet_source_dict = transaction_fee_station_wallet_source_instance.to_dict()
# create an instance of TransactionFeeStationWalletSource from a dict
transaction_fee_station_wallet_source_from_dict = TransactionFeeStationWalletSource.from_dict(transaction_fee_station_wallet_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


