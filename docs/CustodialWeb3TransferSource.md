# CustodialWeb3TransferSource

The information about the transaction source types `Web3`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  You need to provide either the `address` or `included_utxos` property. If neither property is provided, the transfer will fail.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address.  If you want to specify the UTXOs to be used, please provide the &#x60;included_utxos&#x60; property. When &#x60;included_utxos&#x60; is specified, only these specified UTXOs will be used for the transaction. If you specify both the &#x60;address&#x60; and &#x60;included_utxos&#x60; properties, the specified included UTXOs must belong to the address. It is recommended to specify no more than 100 included UTXOs to ensure optimal transaction processing.  You need to provide either the &#x60;address&#x60; or &#x60;included_utxos&#x60; property. If neither property is provided, the transfer will fail.  | [optional] 
**included_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 
**excluded_utxos** | [**List[TransactionUtxo]**](TransactionUtxo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.custodial_web3_transfer_source import CustodialWeb3TransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of CustodialWeb3TransferSource from a JSON string
custodial_web3_transfer_source_instance = CustodialWeb3TransferSource.from_json(json)
# print the JSON string representation of the object
print(CustodialWeb3TransferSource.to_json())

# convert the object into a dict
custodial_web3_transfer_source_dict = custodial_web3_transfer_source_instance.to_dict()
# create an instance of CustodialWeb3TransferSource from a dict
custodial_web3_transfer_source_from_dict = CustodialWeb3TransferSource.from_dict(custodial_web3_transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


