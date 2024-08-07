# TransactionTransferToAddressDestination

Information about the transaction destination type `Address`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransactionDestinationType**](TransactionDestinationType.md) |  | 
**account_output** | [**TransactionTransferToAddressDestinationAccountOutput**](TransactionTransferToAddressDestinationAccountOutput.md) |  | [optional] 
**utxo_outputs** | [**List[TransactionTransferToAddressDestinationUtxoOutputsInner]**](TransactionTransferToAddressDestinationUtxoOutputsInner.md) |  | [optional] 
**change_address** | **str** | The address used to receive the remaining funds or change from the transaction. | [optional] 
**force_internal** | **bool** | Whether the transaction request must be executed as a Loop transfer. For more information about Loop, see [Loop&#39;s website](https://loop.top/).   - &#x60;true&#x60;: The transaction request must be executed as a Loop transfer.   - &#x60;false&#x60;: The transaction request may not be executed as a Loop transfer.  | [optional] 
**force_external** | **bool** | Whether the transaction request must not be executed as a Loop transfer. For more information about Loop, see [Loop&#39;s website](https://loop.top/).   - &#x60;true&#x60;: The transaction request must not be executed as a Loop transfer.   - &#x60;false&#x60;: The transaction request can be executed as a Loop transfer.  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_transfer_to_address_destination import TransactionTransferToAddressDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTransferToAddressDestination from a JSON string
transaction_transfer_to_address_destination_instance = TransactionTransferToAddressDestination.from_json(json)
# print the JSON string representation of the object
print(TransactionTransferToAddressDestination.to_json())

# convert the object into a dict
transaction_transfer_to_address_destination_dict = transaction_transfer_to_address_destination_instance.to_dict()
# create an instance of TransactionTransferToAddressDestination from a dict
transaction_transfer_to_address_destination_from_dict = TransactionTransferToAddressDestination.from_dict(transaction_transfer_to_address_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


