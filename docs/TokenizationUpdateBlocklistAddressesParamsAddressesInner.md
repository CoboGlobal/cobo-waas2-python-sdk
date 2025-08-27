# TokenizationUpdateBlocklistAddressesParamsAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address to add or remove. | 
**note** | **str** | An optional note for the address, primarily used when adding addresses. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_update_blocklist_addresses_params_addresses_inner import TokenizationUpdateBlocklistAddressesParamsAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdateBlocklistAddressesParamsAddressesInner from a JSON string
tokenization_update_blocklist_addresses_params_addresses_inner_instance = TokenizationUpdateBlocklistAddressesParamsAddressesInner.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdateBlocklistAddressesParamsAddressesInner.to_json())

# convert the object into a dict
tokenization_update_blocklist_addresses_params_addresses_inner_dict = tokenization_update_blocklist_addresses_params_addresses_inner_instance.to_dict()
# create an instance of TokenizationUpdateBlocklistAddressesParamsAddressesInner from a dict
tokenization_update_blocklist_addresses_params_addresses_inner_from_dict = TokenizationUpdateBlocklistAddressesParamsAddressesInner.from_dict(tokenization_update_blocklist_addresses_params_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


