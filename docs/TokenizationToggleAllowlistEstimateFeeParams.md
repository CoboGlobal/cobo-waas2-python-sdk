# TokenizationToggleAllowlistEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**activation** | **bool** | Whether to activate the allowlist feature for the token. | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**token_id** | **str** | The ID of the token. | 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_toggle_allowlist_estimate_fee_params import TokenizationToggleAllowlistEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationToggleAllowlistEstimateFeeParams from a JSON string
tokenization_toggle_allowlist_estimate_fee_params_instance = TokenizationToggleAllowlistEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationToggleAllowlistEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_toggle_allowlist_estimate_fee_params_dict = tokenization_toggle_allowlist_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationToggleAllowlistEstimateFeeParams from a dict
tokenization_toggle_allowlist_estimate_fee_params_from_dict = TokenizationToggleAllowlistEstimateFeeParams.from_dict(tokenization_toggle_allowlist_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


