# FiatEntryKycAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The country. | 
**state** | **str** | The state or province. | 
**city** | **str** | The city. | 
**postcode** | **str** | The postal code. | 
**line1** | **str** | The address line. | 

## Example

```python
from cobo_waas2.models.fiat_entry_kyc_address import FiatEntryKycAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FiatEntryKycAddress from a JSON string
fiat_entry_kyc_address_instance = FiatEntryKycAddress.from_json(json)
# print the JSON string representation of the object
print(FiatEntryKycAddress.to_json())

# convert the object into a dict
fiat_entry_kyc_address_dict = fiat_entry_kyc_address_instance.to_dict()
# create an instance of FiatEntryKycAddress from a dict
fiat_entry_kyc_address_from_dict = FiatEntryKycAddress.from_dict(fiat_entry_kyc_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


