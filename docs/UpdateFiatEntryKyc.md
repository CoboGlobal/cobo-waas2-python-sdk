# UpdateFiatEntryKyc

The request body to update fiat entry KYC information.  All fields are optional. Omitted fields keep their existing values. You can pass empty values to clear a field. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_type** | [**FiatEntryKycMerchantType**](FiatEntryKycMerchantType.md) |  | [optional] 
**country** | **str** | The country/region of the fiat entry KYC, in ISO 3166-1 alpha-3 format. | [optional] 
**industry** | **List[str]** | The industry categories of the fiat entry KYC. | [optional] 
**company_info** | [**FiatEntryKycCompanyInfo**](FiatEntryKycCompanyInfo.md) |  | [optional] 
**individual_info** | [**FiatEntryKycPersonInfo**](FiatEntryKycPersonInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.update_fiat_entry_kyc import UpdateFiatEntryKyc

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFiatEntryKyc from a JSON string
update_fiat_entry_kyc_instance = UpdateFiatEntryKyc.from_json(json)
# print the JSON string representation of the object
print(UpdateFiatEntryKyc.to_json())

# convert the object into a dict
update_fiat_entry_kyc_dict = update_fiat_entry_kyc_instance.to_dict()
# create an instance of UpdateFiatEntryKyc from a dict
update_fiat_entry_kyc_from_dict = UpdateFiatEntryKyc.from_dict(update_fiat_entry_kyc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


