# AddressTransferDestinationAccountOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The destination address. | 
**memo** | **str** | The memo that identifies a transaction in order to credit the correct account. For transfers out of Cobo Portal, it is highly recommended to include a memo for the chains such as XRP, EOS, XLM, IOST, BNB_BNB, ATOM, LUNA, and TON. | [optional] 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.address_transfer_destination_account_output import AddressTransferDestinationAccountOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTransferDestinationAccountOutput from a JSON string
address_transfer_destination_account_output_instance = AddressTransferDestinationAccountOutput.from_json(json)
# print the JSON string representation of the object
print(AddressTransferDestinationAccountOutput.to_json())

# convert the object into a dict
address_transfer_destination_account_output_dict = address_transfer_destination_account_output_instance.to_dict()
# create an instance of AddressTransferDestinationAccountOutput from a dict
address_transfer_destination_account_output_from_dict = AddressTransferDestinationAccountOutput.from_dict(address_transfer_destination_account_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


