# TransactionDepositFromAddressSource

Information about the transaction source type `DepositFromAddress`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction sources. 

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


