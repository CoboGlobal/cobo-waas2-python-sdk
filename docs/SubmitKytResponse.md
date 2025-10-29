# SubmitKytResponse

The response for a request to submit a KYT review result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction being processed for KYT screening. | 
**submitted** | **bool** | Indicates whether the KYT review result was successfully submitted. | 

## Example

```python
from cobo_waas2.models.submit_kyt_response import SubmitKytResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitKytResponse from a JSON string
submit_kyt_response_instance = SubmitKytResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitKytResponse.to_json())

# convert the object into a dict
submit_kyt_response_dict = submit_kyt_response_instance.to_dict()
# create an instance of SubmitKytResponse from a dict
submit_kyt_response_from_dict = SubmitKytResponse.from_dict(submit_kyt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


