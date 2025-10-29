# CustodialTransferDestination

The information about the transaction destination type `CustodialWallet`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  **Note: This destination type is deprecated and should no longer be used. Please use `Address` instead.**  Switch between the tabs to display the properties for different transaction destinations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransferDestinationType**](TransferDestinationType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | 

## Example

```python
from cobo_waas2.models.custodial_transfer_destination import CustodialTransferDestination

# TODO update the JSON string below
json = "{}"
# create an instance of CustodialTransferDestination from a JSON string
custodial_transfer_destination_instance = CustodialTransferDestination.from_json(json)
# print the JSON string representation of the object
print(CustodialTransferDestination.to_json())

# convert the object into a dict
custodial_transfer_destination_dict = custodial_transfer_destination_instance.to_dict()
# create an instance of CustodialTransferDestination from a dict
custodial_transfer_destination_from_dict = CustodialTransferDestination.from_dict(custodial_transfer_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


