# TokenizationBlocklistAddressNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address on the blocklist. | 
**note** | **str** | The note for the address on the blocklist. | [optional] 
**created_timestamp** | **int** | The time when the address was added to the blocklist, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_blocklist_address_note import TokenizationBlocklistAddressNote

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationBlocklistAddressNote from a JSON string
tokenization_blocklist_address_note_instance = TokenizationBlocklistAddressNote.from_json(json)
# print the JSON string representation of the object
print(TokenizationBlocklistAddressNote.to_json())

# convert the object into a dict
tokenization_blocklist_address_note_dict = tokenization_blocklist_address_note_instance.to_dict()
# create an instance of TokenizationBlocklistAddressNote from a dict
tokenization_blocklist_address_note_from_dict = TokenizationBlocklistAddressNote.from_dict(tokenization_blocklist_address_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


