# AddressTransferDestination

The information about the transaction destination type `Address`.   Specify either the `account_output` property or the `utxo_outputs` property. You can transfer tokens to multiple addresses only if you use MPC Wallets as the transaction source. You should use the `utxo_outputs` property to specify the destination addresses. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransferDestinationType**](TransferDestinationType.md) |  | 
**account_output** | [**AddressTransferDestinationAccountOutput**](AddressTransferDestinationAccountOutput.md) |  | [optional] 
**utxo_outputs** | [**List[AddressTransferDestinationUtxoOutputsInner]**](AddressTransferDestinationUtxoOutputsInner.md) |  | [optional] 
**change_address** | **str** | The address used to receive the remaining funds or change from the transaction. | [optional] 
**force_internal** | **bool** | Whether the transaction request must be executed as a Loop transfer. For more information about Loop, see [Loop&#39;s website](https://loop.top/).   - &#x60;true&#x60;: The transaction request must be executed as a Loop transfer.   - &#x60;false&#x60;: The transaction request may not be executed as a Loop transfer. &lt;Note&gt;Please do not set both &#x60;force_internal&#x60; and &#x60;force_internal&#x60; as &#x60;true&#x60;.&lt;/Note&gt;  | [optional] 
**force_external** | **bool** | Whether the transaction request must not be executed as a Loop transfer. For more information about Loop, see [Loop&#39;s website](https://loop.top/).   - &#x60;true&#x60;: The transaction request must not be executed as a Loop transfer.   - &#x60;false&#x60;: The transaction request can be executed as a Loop transfer. &lt;Note&gt;Please do not set both &#x60;force_internal&#x60; and &#x60;force_internal&#x60; as &#x60;true&#x60;.&lt;/Note&gt;  | [optional] 

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


