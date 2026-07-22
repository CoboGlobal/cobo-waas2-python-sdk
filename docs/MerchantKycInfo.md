# MerchantKycInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kyc_submission_id** | **str** | The KYC submission ID. | 
**merchant_id** | **str** | The merchant ID. | 
**status** | [**MerchantKycStatus**](MerchantKycStatus.md) |  | 

## Example

```python
from cobo_waas2.models.merchant_kyc_info import MerchantKycInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantKycInfo from a JSON string
merchant_kyc_info_instance = MerchantKycInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantKycInfo.to_json())

# convert the object into a dict
merchant_kyc_info_dict = merchant_kyc_info_instance.to_dict()
# create an instance of MerchantKycInfo from a dict
merchant_kyc_info_from_dict = MerchantKycInfo.from_dict(merchant_kyc_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


