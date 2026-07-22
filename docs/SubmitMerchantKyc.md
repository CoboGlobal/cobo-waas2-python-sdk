# SubmitMerchantKyc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The merchant email address. | 
**phone** | **str** | The merchant phone number. | 
**merchant_type** | [**MerchantKycMerchantType**](MerchantKycMerchantType.md) |  | 
**country** | **str** | The country/region of the merchant, in ISO 3166-1 alpha-3 format. | 
**industry** | **List[str]** | The industry categories of the merchant. | 
**company_info** | [**MerchantKycCompanyInfo**](MerchantKycCompanyInfo.md) |  | 

## Example

```python
from cobo_waas2.models.submit_merchant_kyc import SubmitMerchantKyc

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitMerchantKyc from a JSON string
submit_merchant_kyc_instance = SubmitMerchantKyc.from_json(json)
# print the JSON string representation of the object
print(SubmitMerchantKyc.to_json())

# convert the object into a dict
submit_merchant_kyc_dict = submit_merchant_kyc_instance.to_dict()
# create an instance of SubmitMerchantKyc from a dict
submit_merchant_kyc_from_dict = SubmitMerchantKyc.from_dict(submit_merchant_kyc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


