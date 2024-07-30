# TransactionTransferToAddressDestinationAccountOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The destination address. | [optional] 
**memo** | **str** | The memo that identifies a transaction in order to credit the correct account. For transfers out of Cobo Portal, it is highly recommended to include a memo for the chains such as XRP, EOS, XLM, IOST, BNB_BNB, ATOM, LUNA, and TON. | [optional] 
**amount** | **str** | The quantity of the token in the transaction. For example, if you trade 1.5 ETH, then the value is &#x60;1.5&#x60;.  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_transfer_to_address_destination_account_output import TransactionTransferToAddressDestinationAccountOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTransferToAddressDestinationAccountOutput from a JSON string
transaction_transfer_to_address_destination_account_output_instance = TransactionTransferToAddressDestinationAccountOutput.from_json(json)
# print the JSON string representation of the object
print(TransactionTransferToAddressDestinationAccountOutput.to_json())

# convert the object into a dict
transaction_transfer_to_address_destination_account_output_dict = transaction_transfer_to_address_destination_account_output_instance.to_dict()
# create an instance of TransactionTransferToAddressDestinationAccountOutput from a dict
transaction_transfer_to_address_destination_account_output_from_dict = TransactionTransferToAddressDestinationAccountOutput.from_dict(transaction_transfer_to_address_destination_account_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


