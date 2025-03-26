# TransactionCustodialWeb3WalletSource

Information about the transaction source type `Web3`. Refer to [Transaction sources and destinations](/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | [optional] 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_custodial_web3_wallet_source import TransactionCustodialWeb3WalletSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCustodialWeb3WalletSource from a JSON string
transaction_custodial_web3_wallet_source_instance = TransactionCustodialWeb3WalletSource.from_json(json)
# print the JSON string representation of the object
print(TransactionCustodialWeb3WalletSource.to_json())

# convert the object into a dict
transaction_custodial_web3_wallet_source_dict = transaction_custodial_web3_wallet_source_instance.to_dict()
# create an instance of TransactionCustodialWeb3WalletSource from a dict
transaction_custodial_web3_wallet_source_from_dict = TransactionCustodialWeb3WalletSource.from_dict(transaction_custodial_web3_wallet_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


