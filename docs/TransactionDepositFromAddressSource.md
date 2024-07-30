# TransactionDepositFromAddressSource

Information about the transaction source, which varies depending on whether you are the initiator or the receiver of the transaction.   - As the initiator, you will see detailed information about the transaction source, and the `source` will be displayed as one of the following wallet sub-types: `Asset`, `Org-Controlled`, `User-Controlled`, `Safe{Wallet}`, `Main`, or `Sub`. - As the receiver, you will see the `source` as either `DepositFromAddress`, `DepositFromWallet`, or `DepositFromLoop`. If the transaction is from the Loop transfer network, the source will be `DepositFromLoop`. Otherwise, it will be either `DepositFromWallet` (indicating an Exchange Wallet) or `DepositFromAddress` (indicating other wallet type than an Exchange Wallet or an external address). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**TransactionSourceType**](TransactionSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | [optional] 
**wallet_type** | [**WalletType**](WalletType.md) |  | [optional] 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | [optional] 
**addresses** | **List[str]** | A list of addresses. | 

## Example

```python
from cobo_waas2.models.transaction_deposit_from_address_source import TransactionDepositFromAddressSource

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDepositFromAddressSource from a JSON string
transaction_deposit_from_address_source_instance = TransactionDepositFromAddressSource.from_json(json)
# print the JSON string representation of the object
print(TransactionDepositFromAddressSource.to_json())

# convert the object into a dict
transaction_deposit_from_address_source_dict = transaction_deposit_from_address_source_instance.to_dict()
# create an instance of TransactionDepositFromAddressSource from a dict
transaction_deposit_from_address_source_from_dict = TransactionDepositFromAddressSource.from_dict(transaction_deposit_from_address_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


