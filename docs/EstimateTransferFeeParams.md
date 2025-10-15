# EstimateTransferFeeParams

The information about a token transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. | [optional] 
**request_type** | [**EstimateFeeRequestType**](EstimateFeeRequestType.md) |  | 
**source** | [**TransferSource**](TransferSource.md) |  | 
**token_id** | **str** | The token ID of the transferred token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**destination** | [**TransferDestination**](TransferDestination.md) |  | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | [optional] 
**replaced_transaction_id** | **str** | The ID of the transaction that this transaction replaced. | [optional] 

## Example

```python
from cobo_waas2.models.estimate_transfer_fee_params import EstimateTransferFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateTransferFeeParams from a JSON string
estimate_transfer_fee_params_instance = EstimateTransferFeeParams.from_json(json)
# print the JSON string representation of the object
print(EstimateTransferFeeParams.to_json())

# convert the object into a dict
estimate_transfer_fee_params_dict = estimate_transfer_fee_params_instance.to_dict()
# create an instance of EstimateTransferFeeParams from a dict
estimate_transfer_fee_params_from_dict = EstimateTransferFeeParams.from_dict(estimate_transfer_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


