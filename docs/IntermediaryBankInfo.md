# IntermediaryBankInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_name** | **str** | The name of the intermediary bank. | 
**bank_address** | **str** | The address of the intermediary bank. | 
**bank_swift_code** | **str** | The SWIFT or BIC code of the intermediary bank. | 

## Example

```python
from cobo_waas2.models.intermediary_bank_info import IntermediaryBankInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediaryBankInfo from a JSON string
intermediary_bank_info_instance = IntermediaryBankInfo.from_json(json)
# print the JSON string representation of the object
print(IntermediaryBankInfo.to_json())

# convert the object into a dict
intermediary_bank_info_dict = intermediary_bank_info_instance.to_dict()
# create an instance of IntermediaryBankInfo from a dict
intermediary_bank_info_from_dict = IntermediaryBankInfo.from_dict(intermediary_bank_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


