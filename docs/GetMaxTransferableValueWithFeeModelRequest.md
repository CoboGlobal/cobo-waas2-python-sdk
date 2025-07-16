# GetMaxTransferableValueWithFeeModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID of the transferred token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). For transfers from Exchange Wallets, this property value represents the asset ID. | 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 
**to_address** | **str** | The recipient&#39;s address. | 
**from_address** | **str** | The sender&#39;s address. This property is required when using an EVM address in an MPC Wallet. | [optional] 

## Example

```python
from cobo_waas2.models.get_max_transferable_value_with_fee_model_request import GetMaxTransferableValueWithFeeModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMaxTransferableValueWithFeeModelRequest from a JSON string
get_max_transferable_value_with_fee_model_request_instance = GetMaxTransferableValueWithFeeModelRequest.from_json(json)
# print the JSON string representation of the object
print(GetMaxTransferableValueWithFeeModelRequest.to_json())

# convert the object into a dict
get_max_transferable_value_with_fee_model_request_dict = get_max_transferable_value_with_fee_model_request_instance.to_dict()
# create an instance of GetMaxTransferableValueWithFeeModelRequest from a dict
get_max_transferable_value_with_fee_model_request_from_dict = GetMaxTransferableValueWithFeeModelRequest.from_dict(get_max_transferable_value_with_fee_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


