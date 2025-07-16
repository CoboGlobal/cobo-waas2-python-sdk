# MaxTransferableValue

The maximum transferable value from the wallet or the specified address, along with the estimated transaction fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
**max_transferable_value** | **str** | The maximum transferable value from the wallet or the specified address. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.max_transferable_value import MaxTransferableValue

# TODO update the JSON string below
json = "{}"
# create an instance of MaxTransferableValue from a JSON string
max_transferable_value_instance = MaxTransferableValue.from_json(json)
# print the JSON string representation of the object
print(MaxTransferableValue.to_json())

# convert the object into a dict
max_transferable_value_dict = max_transferable_value_instance.to_dict()
# create an instance of MaxTransferableValue from a dict
max_transferable_value_from_dict = MaxTransferableValue.from_dict(max_transferable_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


