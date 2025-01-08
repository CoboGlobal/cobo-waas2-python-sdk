# TransferParams

The information about a token transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | 
**source** | [**TransferSource**](TransferSource.md) |  | 
**token_id** | **str** | The token ID of the transferred token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). For transfers from Exchange Wallets, this property value represents the asset ID. | 
**destination** | [**TransferDestination**](TransferDestination.md) |  | 
**category_names** | **List[str]** | The custom category for you to identify your transactions. | [optional] 
**description** | **str** | The description of the transfer. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 
**auto_fuel** | [**AutoFuelType**](AutoFuelType.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transfer_params import TransferParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransferParams from a JSON string
transfer_params_instance = TransferParams.from_json(json)
# print the JSON string representation of the object
print(TransferParams.to_json())

# convert the object into a dict
transfer_params_dict = transfer_params_instance.to_dict()
# create an instance of TransferParams from a dict
transfer_params_from_dict = TransferParams.from_dict(transfer_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


