# MerchantKycCompanyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_type** | [**MerchantKycCompanyType**](MerchantKycCompanyType.md) |  | 
**listed** | **bool** | Whether the company is listed. | 
**attachments** | [**List[MerchantKycCompanyAttachment]**](MerchantKycCompanyAttachment.md) | The attachments of the company. | 
**operation_address** | [**MerchantKycAddress**](MerchantKycAddress.md) |  | 
**identify_no** | **str** | The company identification number. | 
**company_name** | **str** | The company name in local language. | 
**company_name_en** | **str** | The company name in English. | 
**establish_date** | **str** | The establishment date of the company. | 
**commencement_date** | **str** | The commencement date of the company. | 
**valid_period** | **str** | The valid period of the company registration. | 
**register_address** | [**MerchantKycAddress**](MerchantKycAddress.md) |  | 
**legal_info** | [**MerchantKycPersonInfo**](MerchantKycPersonInfo.md) |  | 
**ubo_infos** | [**List[MerchantKycPersonInfo]**](MerchantKycPersonInfo.md) | The ultimate beneficial owner information. | 
**online_store_url** | **str** | The online store URL. Required when merchant type is B2B. | [optional] 

## Example

```python
from cobo_waas2.models.merchant_kyc_company_info import MerchantKycCompanyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantKycCompanyInfo from a JSON string
merchant_kyc_company_info_instance = MerchantKycCompanyInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantKycCompanyInfo.to_json())

# convert the object into a dict
merchant_kyc_company_info_dict = merchant_kyc_company_info_instance.to_dict()
# create an instance of MerchantKycCompanyInfo from a dict
merchant_kyc_company_info_from_dict = MerchantKycCompanyInfo.from_dict(merchant_kyc_company_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


