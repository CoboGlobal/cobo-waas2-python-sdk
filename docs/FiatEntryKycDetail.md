# FiatEntryKycDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiat_entry_kyc_id** | **str** | The fiat entry KYC ID. | 
**status** | [**FiatEntryKycStatus**](FiatEntryKycStatus.md) |  | 
**merchant_type** | [**FiatEntryKycMerchantType**](FiatEntryKycMerchantType.md) |  | 
**country** | **str** | The country/region of the fiat entry KYC, in ISO 3166-1 alpha-3 format. | 
**industry** | **List[str]** | The industry categories of the fiat entry KYC. | 
**email** | **str** | The email address. | [optional] 
**phone** | **str** | The phone number. | [optional] 
**company_info** | [**FiatEntryKycCompanyInfo**](FiatEntryKycCompanyInfo.md) |  | [optional] 
**individual_info** | [**FiatEntryKycPersonInfo**](FiatEntryKycPersonInfo.md) |  | [optional] 
**created_timestamp** | **int** | The creation timestamp in Unix seconds. | 
**updated_timestamp** | **int** | The last update timestamp in Unix seconds. | [optional] 

## Example

```python
from cobo_waas2.models.fiat_entry_kyc_detail import FiatEntryKycDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FiatEntryKycDetail from a JSON string
fiat_entry_kyc_detail_instance = FiatEntryKycDetail.from_json(json)
# print the JSON string representation of the object
print(FiatEntryKycDetail.to_json())

# convert the object into a dict
fiat_entry_kyc_detail_dict = fiat_entry_kyc_detail_instance.to_dict()
# create an instance of FiatEntryKycDetail from a dict
fiat_entry_kyc_detail_from_dict = FiatEntryKycDetail.from_dict(fiat_entry_kyc_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


