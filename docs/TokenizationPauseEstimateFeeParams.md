# TokenizationPauseEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**token_id** | **str** | The ID of the token. | 

## Example

```python
from cobo_waas2.models.tokenization_pause_estimate_fee_params import TokenizationPauseEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationPauseEstimateFeeParams from a JSON string
tokenization_pause_estimate_fee_params_instance = TokenizationPauseEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationPauseEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_pause_estimate_fee_params_dict = tokenization_pause_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationPauseEstimateFeeParams from a dict
tokenization_pause_estimate_fee_params_from_dict = TokenizationPauseEstimateFeeParams.from_dict(tokenization_pause_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


