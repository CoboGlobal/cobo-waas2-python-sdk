# MerchantKycAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The country. | 
**state** | **str** | The state or province. | 
**city** | **str** | The city. | 
**postcode** | **str** | The postal code. | 
**line1** | **str** | The address line. | 

## Example

```python
from cobo_waas2.models.merchant_kyc_address import MerchantKycAddress

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantKycAddress from a JSON string
merchant_kyc_address_instance = MerchantKycAddress.from_json(json)
# print the JSON string representation of the object
print(MerchantKycAddress.to_json())

# convert the object into a dict
merchant_kyc_address_dict = merchant_kyc_address_instance.to_dict()
# create an instance of MerchantKycAddress from a dict
merchant_kyc_address_from_dict = MerchantKycAddress.from_dict(merchant_kyc_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


