# FiatEntryKycPersonInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name or title of an identification document. | 
**name_en** | **str** | The English-language equivalent of the identification document&#39;s name. | 
**id_number** | **str** | The unique identification number associated with the identification document. | 
**date_of_birth** | **str** | The date of birth of the individual, usually in the format YYYYMMDD.  | 
**issue_date** | **str** | The issue date refers to the date when a document, such as an identification card or passport, was officially issued or granted, usually in the format YYYYMMDD.  | 
**expiration_date** | **str** | The expiration date refers to the date when a document, such as an identification card or passport, is no longer valid or legally usable, usually in the format YYYYMMDD.  | 
**attachments** | [**List[FiatEntryKycPersonAttachment]**](FiatEntryKycPersonAttachment.md) | Additional files or documents associated with a message or record to provide extra information or context.  | 
**residential_address** | [**FiatEntryKycAddress**](FiatEntryKycAddress.md) |  | 

## Example

```python
from cobo_waas2.models.fiat_entry_kyc_person_info import FiatEntryKycPersonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FiatEntryKycPersonInfo from a JSON string
fiat_entry_kyc_person_info_instance = FiatEntryKycPersonInfo.from_json(json)
# print the JSON string representation of the object
print(FiatEntryKycPersonInfo.to_json())

# convert the object into a dict
fiat_entry_kyc_person_info_dict = fiat_entry_kyc_person_info_instance.to_dict()
# create an instance of FiatEntryKycPersonInfo from a dict
fiat_entry_kyc_person_info_from_dict = FiatEntryKycPersonInfo.from_dict(fiat_entry_kyc_person_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


