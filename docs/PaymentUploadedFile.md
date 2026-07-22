# PaymentUploadedFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | The AWS file link of the uploaded file. | 
**expired_timestamp** | **int** | The time when the uploaded file link expires, in Unix timestamp format, measured in milliseconds. | 

## Example

```python
from cobo_waas2.models.payment_uploaded_file import PaymentUploadedFile

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentUploadedFile from a JSON string
payment_uploaded_file_instance = PaymentUploadedFile.from_json(json)
# print the JSON string representation of the object
print(PaymentUploadedFile.to_json())

# convert the object into a dict
payment_uploaded_file_dict = payment_uploaded_file_instance.to_dict()
# create an instance of PaymentUploadedFile from a dict
payment_uploaded_file_from_dict = PaymentUploadedFile.from_dict(payment_uploaded_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


