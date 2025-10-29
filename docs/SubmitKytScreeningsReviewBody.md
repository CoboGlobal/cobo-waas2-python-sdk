# SubmitKytScreeningsReviewBody

The information about submitting a manual KYT review result for KYT screening cases that require human analysis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction that requires a manual KYT review. | 
**result** | [**KytScreeningsReviewType**](KytScreeningsReviewType.md) |  | 

## Example

```python
from cobo_waas2.models.submit_kyt_screenings_review_body import SubmitKytScreeningsReviewBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitKytScreeningsReviewBody from a JSON string
submit_kyt_screenings_review_body_instance = SubmitKytScreeningsReviewBody.from_json(json)
# print the JSON string representation of the object
print(SubmitKytScreeningsReviewBody.to_json())

# convert the object into a dict
submit_kyt_screenings_review_body_dict = submit_kyt_screenings_review_body_instance.to_dict()
# create an instance of SubmitKytScreeningsReviewBody from a dict
submit_kyt_screenings_review_body_from_dict = SubmitKytScreeningsReviewBody.from_dict(submit_kyt_screenings_review_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


