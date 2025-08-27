# TokenizationAllowlistAddressNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address on the allowlist. | 
**note** | **str** | The note for the address on the allowlist. | [optional] 
**created_timestamp** | **int** | The time when the address was added to the allowlist, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_allowlist_address_note import TokenizationAllowlistAddressNote

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationAllowlistAddressNote from a JSON string
tokenization_allowlist_address_note_instance = TokenizationAllowlistAddressNote.from_json(json)
# print the JSON string representation of the object
print(TokenizationAllowlistAddressNote.to_json())

# convert the object into a dict
tokenization_allowlist_address_note_dict = tokenization_allowlist_address_note_instance.to_dict()
# create an instance of TokenizationAllowlistAddressNote from a dict
tokenization_allowlist_address_note_from_dict = TokenizationAllowlistAddressNote.from_dict(tokenization_allowlist_address_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


