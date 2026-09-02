# PaymentUploadFileV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The original file name, including the file extension. | 
**file_content** | **str** | The file content, encoded in Base64. | 

## Example

```python
from cobo_waas2.models.payment_upload_file_v2 import PaymentUploadFileV2

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentUploadFileV2 from a JSON string
payment_upload_file_v2_instance = PaymentUploadFileV2.from_json(json)
# print the JSON string representation of the object
print(PaymentUploadFileV2.to_json())

# convert the object into a dict
payment_upload_file_v2_dict = payment_upload_file_v2_instance.to_dict()
# create an instance of PaymentUploadFileV2 from a dict
payment_upload_file_v2_from_dict = PaymentUploadFileV2.from_dict(payment_upload_file_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


