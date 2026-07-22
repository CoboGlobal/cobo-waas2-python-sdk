# MerchantKycCompanyAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The AWS file link of the uploaded file, which you can retrieve by calling [Upload file](https://www.cobo.com/developers/v2/api-references/payment/upload-file).  | 
**file_type** | [**MerchantKycCompanyAttachmentFileType**](MerchantKycCompanyAttachmentFileType.md) |  | 

## Example

```python
from cobo_waas2.models.merchant_kyc_company_attachment import MerchantKycCompanyAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantKycCompanyAttachment from a JSON string
merchant_kyc_company_attachment_instance = MerchantKycCompanyAttachment.from_json(json)
# print the JSON string representation of the object
print(MerchantKycCompanyAttachment.to_json())

# convert the object into a dict
merchant_kyc_company_attachment_dict = merchant_kyc_company_attachment_instance.to_dict()
# create an instance of MerchantKycCompanyAttachment from a dict
merchant_kyc_company_attachment_from_dict = MerchantKycCompanyAttachment.from_dict(merchant_kyc_company_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


