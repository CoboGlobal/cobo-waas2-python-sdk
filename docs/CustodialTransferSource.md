# CustodialTransferSource

The information about the transaction source types `Asset`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction sources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WalletSubtype**](WalletSubtype.md) |  | 
**wallet_id** | **str** | The wallet ID. | 

## Example

```python
from cobo_waas2.models.custodial_transfer_source import CustodialTransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of CustodialTransferSource from a JSON string
custodial_transfer_source_instance = CustodialTransferSource.from_json(json)
# print the JSON string representation of the object
print(CustodialTransferSource.to_json())

# convert the object into a dict
custodial_transfer_source_dict = custodial_transfer_source_instance.to_dict()
# create an instance of CustodialTransferSource from a dict
custodial_transfer_source_from_dict = CustodialTransferSource.from_dict(custodial_transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


