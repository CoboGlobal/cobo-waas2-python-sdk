# TransactionWalletConnectInfo

The extra information of transaction initiated by walletconnect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_type** | [**TransactionExtraType**](TransactionExtraType.md) |  | 
**dapp_name** | **str** | The dapp name that initiated this transaction. | [optional] 
**dapp_domain** | **str** | The dapp domain that initiated this transaction | [optional] 
**session_id** | **str** | The session id that initiated this transaction | [optional] 

## Example

```python
from cobo_waas2.models.transaction_wallet_connect_info import TransactionWalletConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWalletConnectInfo from a JSON string
transaction_wallet_connect_info_instance = TransactionWalletConnectInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionWalletConnectInfo.to_json())

# convert the object into a dict
transaction_wallet_connect_info_dict = transaction_wallet_connect_info_instance.to_dict()
# create an instance of TransactionWalletConnectInfo from a dict
transaction_wallet_connect_info_from_dict = TransactionWalletConnectInfo.from_dict(transaction_wallet_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


