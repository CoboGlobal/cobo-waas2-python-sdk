# MerchantKycPersonInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name or title of an identification document. | 
**name_en** | **str** | The English-language equivalent of the identification document&#39;s name. | 
**id_number** | **str** | The unique identification number associated with the identification document. | 
**date_of_birth** | **str** | The date of birth of the individual, usually in the format YYYYMMDD.  | 
**issue_date** | **str** | The issue date refers to the date when a document, such as an identification card or passport, was officially issued or granted, usually in the format YYYYMMDD.  | 
**expiration_date** | **str** | The expiration date refers to the date when a document, such as an identification card or passport, is no longer valid or legally usable, usually in the format YYYYMMDD.  | 
**attachments** | [**List[MerchantKycPersonAttachment]**](MerchantKycPersonAttachment.md) | Additional files or documents associated with a message or record to provide extra information or context.  | 
**residential_address** | [**MerchantKycAddress**](MerchantKycAddress.md) |  | 

## Example

```python
from cobo_waas2.models.merchant_kyc_person_info import MerchantKycPersonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantKycPersonInfo from a JSON string
merchant_kyc_person_info_instance = MerchantKycPersonInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantKycPersonInfo.to_json())

# convert the object into a dict
merchant_kyc_person_info_dict = merchant_kyc_person_info_instance.to_dict()
# create an instance of MerchantKycPersonInfo from a dict
merchant_kyc_person_info_from_dict = MerchantKycPersonInfo.from_dict(merchant_kyc_person_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


