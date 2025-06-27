# TokenizationUpdateAllowlistAddressesParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TokenizationUpdateAddressAction**](TokenizationUpdateAddressAction.md) |  | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**addresses** | [**List[TokenizationUpdateAllowlistAddressesParamsAddressesInner]**](TokenizationUpdateAllowlistAddressesParamsAddressesInner.md) | A list of addresses to manage. For &#39;add&#39; operations, notes can be provided. For &#39;remove&#39; operations, notes are ignored. | 

## Example

```python
from cobo_waas2.models.tokenization_update_allowlist_addresses_params import TokenizationUpdateAllowlistAddressesParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdateAllowlistAddressesParams from a JSON string
tokenization_update_allowlist_addresses_params_instance = TokenizationUpdateAllowlistAddressesParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdateAllowlistAddressesParams.to_json())

# convert the object into a dict
tokenization_update_allowlist_addresses_params_dict = tokenization_update_allowlist_addresses_params_instance.to_dict()
# create an instance of TokenizationUpdateAllowlistAddressesParams from a dict
tokenization_update_allowlist_addresses_params_from_dict = TokenizationUpdateAllowlistAddressesParams.from_dict(tokenization_update_allowlist_addresses_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


