# TransactionCustodialAssetWalletSource

Information about the transaction source type `Asset`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 

## Example

```python
from cobo_waas2.models.transaction_custodial_asset_wallet_source import TransactionCustodialAssetWalletSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCustodialAssetWalletSource from a JSON string
transaction_custodial_asset_wallet_source_instance = TransactionCustodialAssetWalletSource.from_json(json)
# print the JSON string representation of the object
print(TransactionCustodialAssetWalletSource.to_json())

# convert the object into a dict
transaction_custodial_asset_wallet_source_dict = transaction_custodial_asset_wallet_source_instance.to_dict()
# create an instance of TransactionCustodialAssetWalletSource from a dict
transaction_custodial_asset_wallet_source_from_dict = TransactionCustodialAssetWalletSource.from_dict(transaction_custodial_asset_wallet_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


