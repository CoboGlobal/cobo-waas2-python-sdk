# CreateFiatEntryKyc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_type** | [**FiatEntryKycMerchantType**](FiatEntryKycMerchantType.md) |  | 
**country** | **str** | The country/region of the fiat entry KYC, in ISO 3166-1 alpha-3 format. | 
**industry** | **List[str]** | The industry categories of the fiat entry KYC. | 
**company_info** | [**FiatEntryKycCompanyInfo**](FiatEntryKycCompanyInfo.md) |  | [optional] 
**individual_info** | [**FiatEntryKycPersonInfo**](FiatEntryKycPersonInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_fiat_entry_kyc import CreateFiatEntryKyc

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFiatEntryKyc from a JSON string
create_fiat_entry_kyc_instance = CreateFiatEntryKyc.from_json(json)
# print the JSON string representation of the object
print(CreateFiatEntryKyc.to_json())

# convert the object into a dict
create_fiat_entry_kyc_dict = create_fiat_entry_kyc_instance.to_dict()
# create an instance of CreateFiatEntryKyc from a dict
create_fiat_entry_kyc_from_dict = CreateFiatEntryKyc.from_dict(create_fiat_entry_kyc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


