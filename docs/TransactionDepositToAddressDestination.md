# TransactionDepositToAddressDestination

Information about the transaction destination type `DepositToAddress`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**wallet_type** | [**WalletType**](WalletType.md) |  | 
**wallet_subtype** | [**WalletSubtype**](WalletSubtype.md) |  | [optional] 
**address** | **str** | The destination address. | 
**memo** | **str** | The memo that identifies a transaction in order to credit the correct account. For transfers out of Cobo Portal, it is highly recommended to include a memo for the chains such as XRP, EOS, XLM, IOST, BNB_BNB, ATOM, LUNA, and TON. | [optional] 
**amount** | **str** | The quantity of the token in the transaction. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.transaction_deposit_to_address_destination import TransactionDepositToAddressDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDepositToAddressDestination from a JSON string
transaction_deposit_to_address_destination_instance = TransactionDepositToAddressDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionDepositToAddressDestination.to_json())

# convert the object into a dict
transaction_deposit_to_address_destination_dict = transaction_deposit_to_address_destination_instance.to_dict()
# create an instance of TransactionDepositToAddressDestination from a dict
transaction_deposit_to_address_destination_from_dict = TransactionDepositToAddressDestination.from_dict(transaction_deposit_to_address_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


