# TokenizationAllowlistActivationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**activation** | **bool** | Whether to activate the allowlist feature for the token. | 

## Example

```python
from cobo_waas2.models.tokenization_allowlist_activation_params import TokenizationAllowlistActivationParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationAllowlistActivationParams from a JSON string
tokenization_allowlist_activation_params_instance = TokenizationAllowlistActivationParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationAllowlistActivationParams.to_json())

# convert the object into a dict
tokenization_allowlist_activation_params_dict = tokenization_allowlist_activation_params_instance.to_dict()
# create an instance of TokenizationAllowlistActivationParams from a dict
tokenization_allowlist_activation_params_from_dict = TokenizationAllowlistActivationParams.from_dict(tokenization_allowlist_activation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


