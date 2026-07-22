# MerchantKycSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kyc_submission_id** | **str** | The KYC submission ID. | 
**merchant_id** | **str** | The merchant ID. | 
**status** | [**MerchantKycStatus**](MerchantKycStatus.md) |  | 
**email** | **str** | The merchant email address. | 
**phone** | **str** | The merchant phone number. | 
**merchant_type** | [**MerchantKycMerchantType**](MerchantKycMerchantType.md) |  | 
**country** | **str** | The country/region of the merchant, in ISO 3166-1 alpha-3 format. | 
**industry** | **List[str]** | The industry categories of the merchant. | 
**company_info** | [**MerchantKycCompanyInfo**](MerchantKycCompanyInfo.md) |  | 
**created_timestamp** | **int** | The creation timestamp in Unix seconds. | 
**updated_timestamp** | **int** | The last update timestamp in Unix seconds. | [optional] 

## Example

```python
from cobo_waas2.models.merchant_kyc_submission import MerchantKycSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantKycSubmission from a JSON string
merchant_kyc_submission_instance = MerchantKycSubmission.from_json(json)
# print the JSON string representation of the object
print(MerchantKycSubmission.to_json())

# convert the object into a dict
merchant_kyc_submission_dict = merchant_kyc_submission_instance.to_dict()
# create an instance of MerchantKycSubmission from a dict
merchant_kyc_submission_from_dict = MerchantKycSubmission.from_dict(merchant_kyc_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


