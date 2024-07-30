# TransactionMPCWalletSource

Information about the transaction source, which varies depending on whether you are the initiator or the receiver of the transaction.   - As the initiator, you will see detailed information about the transaction source, and the `source` will be displayed as one of the following wallet sub-types: `Asset`, `Org-Controlled`, `User-Controlled`, `Safe{Wallet}`, `Main`, or `Sub`. - As the receiver, you will see the `source` as either `DepositFromAddress`, `DepositFromWallet`, or `DepositFromLoop`. If the transaction is from the Loop transfer network, the source will be `DepositFromLoop`. Otherwise, it will be either `DepositFromWallet` (indicating an Exchange Wallet) or `DepositFromAddress` (indicating other wallet type than an Exchange Wallet or an external address). 

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
from cobo_waas2.models.transaction_mpc_wallet_source import TransactionMPCWalletSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMPCWalletSource from a JSON string
transaction_mpc_wallet_source_instance = TransactionMPCWalletSource.from_json(json)
# print the JSON string representation of the object
print(TransactionMPCWalletSource.to_json())

# convert the object into a dict
transaction_mpc_wallet_source_dict = transaction_mpc_wallet_source_instance.to_dict()
# create an instance of TransactionMPCWalletSource from a dict
transaction_mpc_wallet_source_from_dict = TransactionMPCWalletSource.from_dict(transaction_mpc_wallet_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


