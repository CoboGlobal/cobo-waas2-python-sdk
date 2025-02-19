# TransactionDepositToAddressDestinationTxInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vout_n** | **int** | The output index of the UTXO. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_deposit_to_address_destination_tx_info import TransactionDepositToAddressDestinationTxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDepositToAddressDestinationTxInfo from a JSON string
transaction_deposit_to_address_destination_tx_info_instance = TransactionDepositToAddressDestinationTxInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionDepositToAddressDestinationTxInfo.to_json())

# convert the object into a dict
transaction_deposit_to_address_destination_tx_info_dict = transaction_deposit_to_address_destination_tx_info_instance.to_dict()
# create an instance of TransactionDepositToAddressDestinationTxInfo from a dict
transaction_deposit_to_address_destination_tx_info_from_dict = TransactionDepositToAddressDestinationTxInfo.from_dict(transaction_deposit_to_address_destination_tx_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


