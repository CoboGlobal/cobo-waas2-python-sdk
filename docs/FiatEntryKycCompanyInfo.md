# FiatEntryKycCompanyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_type** | [**FiatEntryKycCompanyType**](FiatEntryKycCompanyType.md) |  | 
**listed** | **bool** | Whether the company is listed. | 
**attachments** | [**List[FiatEntryKycCompanyAttachment]**](FiatEntryKycCompanyAttachment.md) | The attachments of the company. | 
**operation_address** | [**FiatEntryKycAddress**](FiatEntryKycAddress.md) |  | 
**identify_no** | **str** | The company identification number. | 
**company_name** | **str** | The company name in local language. | 
**company_name_en** | **str** | The company name in English. | 
**establish_date** | **str** | The establishment date of the company. | 
**commencement_date** | **str** | The commencement date of the company. | 
**valid_period** | **str** | The valid period of the company registration. | 
**register_address** | [**FiatEntryKycAddress**](FiatEntryKycAddress.md) |  | 
**legal_info** | [**FiatEntryKycPersonInfo**](FiatEntryKycPersonInfo.md) |  | 
**ubo_infos** | [**List[FiatEntryKycPersonInfo]**](FiatEntryKycPersonInfo.md) | The ultimate beneficial owner information. | 
**online_store_url** | **str** | The online store URL. Required when merchant type is B2B. | [optional] 

## Example

```python
from cobo_waas2.models.fiat_entry_kyc_company_info import FiatEntryKycCompanyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FiatEntryKycCompanyInfo from a JSON string
fiat_entry_kyc_company_info_instance = FiatEntryKycCompanyInfo.from_json(json)
# print the JSON string representation of the object
print(FiatEntryKycCompanyInfo.to_json())

# convert the object into a dict
fiat_entry_kyc_company_info_dict = fiat_entry_kyc_company_info_instance.to_dict()
# create an instance of FiatEntryKycCompanyInfo from a dict
fiat_entry_kyc_company_info_from_dict = FiatEntryKycCompanyInfo.from_dict(fiat_entry_kyc_company_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


