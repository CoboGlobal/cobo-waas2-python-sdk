# TokenizationUpdateAllowlistAddressesEstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TokenizationUpdateAddressAction**](TokenizationUpdateAddressAction.md) |  | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**addresses** | [**List[TokenizationUpdateAllowlistAddressesParamsAddressesInner]**](TokenizationUpdateAllowlistAddressesParamsAddressesInner.md) | A list of addresses to manage. For &#39;add&#39; operations, notes can be provided. For &#39;remove&#39; operations, notes are ignored. | 
**operation_type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**token_id** | **str** | The ID of the token. | 

## Example

```python
from cobo_waas2.models.tokenization_update_allowlist_addresses_estimate_fee_params import TokenizationUpdateAllowlistAddressesEstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdateAllowlistAddressesEstimateFeeParams from a JSON string
tokenization_update_allowlist_addresses_estimate_fee_params_instance = TokenizationUpdateAllowlistAddressesEstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdateAllowlistAddressesEstimateFeeParams.to_json())

# convert the object into a dict
tokenization_update_allowlist_addresses_estimate_fee_params_dict = tokenization_update_allowlist_addresses_estimate_fee_params_instance.to_dict()
# create an instance of TokenizationUpdateAllowlistAddressesEstimateFeeParams from a dict
tokenization_update_allowlist_addresses_estimate_fee_params_from_dict = TokenizationUpdateAllowlistAddressesEstimateFeeParams.from_dict(tokenization_update_allowlist_addresses_estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


