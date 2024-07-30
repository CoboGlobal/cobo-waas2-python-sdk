# AddressTransferDestination

The information about the transaction destination. Specify either the `account_output` property or the `utxo_outputs` property. Only MPC Wallets as the transaction source can transfer tokens to multiple addresses by using the `utxo_outputs` property. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransferDestinationType**](TransferDestinationType.md) |  | 
**account_output** | [**AddressTransferDestinationAccountOutput**](AddressTransferDestinationAccountOutput.md) |  | [optional] 
**utxo_outputs** | [**List[AddressTransferDestinationUtxoOutputsInner]**](AddressTransferDestinationUtxoOutputsInner.md) |  | [optional] 
**change_address** | **str** | The address used to receive the remaining funds or change from the transaction. | [optional] 
**force_internal** | **bool** | Whether the transaction request must be executed as a Loop transfer. For more information about Loop, see [Loop&#39;s website](https://loop.top/).   - &#x60;true&#x60;: The transaction request must be executed as a Loop transfer.   - &#x60;false&#x60;: The transaction request may not be executed as a Loop transfer.  | [optional] 
**force_external** | **bool** | Whether the transaction request must not be executed as a Loop transfer. For more information about Loop, see [Loop&#39;s website](https://loop.top/).   - &#x60;true&#x60;: The transaction request must not be executed as a Loop transfer.   - &#x60;false&#x60;: The transaction request can be executed as a Loop transfer.  | [optional] 

## Example

```python
from cobo_waas2.models.address_transfer_destination import AddressTransferDestination

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTransferDestination from a JSON string
address_transfer_destination_instance = AddressTransferDestination.from_json(json)
# print the JSON string representation of the object
print(AddressTransferDestination.to_json())

# convert the object into a dict
address_transfer_destination_dict = address_transfer_destination_instance.to_dict()
# create an instance of AddressTransferDestination from a dict
address_transfer_destination_from_dict = AddressTransferDestination.from_dict(address_transfer_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


