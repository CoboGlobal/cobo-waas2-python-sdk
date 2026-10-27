# FiatEntryKycCompanyAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The file ID of the uploaded file, which you can retrieve by calling [Upload file v2](https://www.cobo.com/developers/v2/api-references/payment/upload-file-v2).  | 
**file_type** | [**FiatEntryKycCompanyAttachmentFileType**](FiatEntryKycCompanyAttachmentFileType.md) |  | 

## Example

```python
from cobo_waas2.models.fiat_entry_kyc_company_attachment import FiatEntryKycCompanyAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of FiatEntryKycCompanyAttachment from a JSON string
fiat_entry_kyc_company_attachment_instance = FiatEntryKycCompanyAttachment.from_json(json)
# print the JSON string representation of the object
print(FiatEntryKycCompanyAttachment.to_json())

# convert the object into a dict
fiat_entry_kyc_company_attachment_dict = fiat_entry_kyc_company_attachment_instance.to_dict()
# create an instance of FiatEntryKycCompanyAttachment from a dict
fiat_entry_kyc_company_attachment_from_dict = FiatEntryKycCompanyAttachment.from_dict(fiat_entry_kyc_company_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


